import re

import json

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from config.config import (OPENAI_AZURE_ENDPOINT, OPENAI_API_VERSION, OPENAI_DEPLOYMENT_NAME, OPENAI_API_KEY, OPENAI_API_TYPE, OPENAI_MODEL_NAME)
from openai_functions.config import (AKKANTO_GPT_PROMPT_TEMPLATE, OUTPUT_TEMPLATE_JSON, METADATA, create_output_template_json)

from openai_functions.prompts_LP import (AKKANTO_LAW_PROPOSAL_PROMPT)
from openai_functions.prompts_OQ import (AKKANTO_ORAL_QUESTION_PROMPT)
from openai_functions.prompts_VOM import (AKKANTO_VOTE_ON_MOTIONS_PROMPT, OUTPUT_TEMPLATE_JSON_VOTE_ON_MOTION)
from openai_functions.prompts_SUG import (AKKANTO_SUGGESTION_PROMPT)
from openai_functions.prompts_WQ import (AKKANTO_WRITTEN_QUESTION_PROMPT)
from openai_functions.prompts_HE import (AKKANTO_HEARING_PROMPT)

def generate_output_type_by_type(pages, date_scraped, cloud_metadata):
    RUNNING_CONFIG = {
        "Law proposal": {"prompt": AKKANTO_LAW_PROPOSAL_PROMPT, "output_template": create_output_template_json("Law Proposal")},
        "Oral Question": {"prompt": AKKANTO_ORAL_QUESTION_PROMPT, "output_template": create_output_template_json("Oral Question")},
        "Vote on Motions": {"prompt": AKKANTO_VOTE_ON_MOTIONS_PROMPT, "output_template": OUTPUT_TEMPLATE_JSON_VOTE_ON_MOTION},
        # "Suggestion": {"prompt": AKKANTO_SUGGESTION_PROMPT, "output_template": create_output_template_json("Suggestion")},
        # "Written Question": {"prompt": AKKANTO_WRITTEN_QUESTION_PROMPT, "output_template": create_output_template_json("Written Question")},
        # "Hearing": {"prompt": AKKANTO_HEARING_PROMPT, "output_template": create_output_template_json("Hearing")}
    }

    chat = AzureChatOpenAI(
                    azure_endpoint=OPENAI_AZURE_ENDPOINT,
                    openai_api_version=OPENAI_API_VERSION,
                    deployment_name=OPENAI_DEPLOYMENT_NAME,
                    openai_api_key=OPENAI_API_KEY,
                    openai_api_type=OPENAI_API_TYPE,
                    model_name=OPENAI_MODEL_NAME,
                    streaming=False,
                    temperature=0)
    
    full_document = " ".join(pages) # TODO: remove slice

    result_all_topics, result_tmp = [], []
    for key in RUNNING_CONFIG.keys():
        
        prompt2 = PromptTemplate.from_template(RUNNING_CONFIG[key]["prompt"])  
        
        chain = LLMChain(
                        llm=chat, 
                        verbose=False, 
                        prompt=prompt2)

        result_raw = chain.run(document_content=full_document,
                            output_template_json = RUNNING_CONFIG[key]["output_template"],
                            topics=METADATA["topics"])
        
        # Clean the result
        result_sliced=result_raw[result_raw.find("["):result_raw.rfind(']')+1]
        result_sliced=re.sub(' +', ' ', result_sliced)
        result_sliced=re.sub('\n', '', result_sliced)

        if result_sliced != "[]":
            result_cleaned = []
            result_tmp = json.loads(result_sliced)
            
            # Add metadata
            for j in range(len(result_tmp)):
                if (result_tmp[j]["issue_fr"] != "/" or result_tmp[j]["issue_nl"] != "/"):
                    # result_tmp[j]["page"] = i + 1 

                    result_tmp[j]["type"] = key
                    result_tmp[j]["filename"] = cloud_metadata["filename"]
                    result_tmp[j]["policy_level_fr"] = cloud_metadata["policy_level_fr"]
                    result_tmp[j]["policy_level_nl"] = cloud_metadata["policy_level_nl"]
                    result_tmp[j]["date_scraped"] = date_scraped
                    result_cleaned += [result_tmp[j]]

            result_all_topics += result_cleaned

    return result_all_topics, result_tmp


def generate_output_page_by_page(pages, date_scraped, cloud_metadata):  
    chat = AzureChatOpenAI(
                azure_endpoint=OPENAI_AZURE_ENDPOINT,
                openai_api_version=OPENAI_API_VERSION,
                deployment_name=OPENAI_DEPLOYMENT_NAME,
                openai_api_key=OPENAI_API_KEY,
                openai_api_type=OPENAI_API_TYPE,
                model_name=OPENAI_MODEL_NAME,
                streaming=False,
                temperature=0)
            
    prompt2 = PromptTemplate.from_template(AKKANTO_GPT_PROMPT_TEMPLATE)  
    
    chain = LLMChain(
                    llm=chat, 
                    verbose=False, 
                    prompt=prompt2)
    
    results, raw_results = [], []

    for i, page in enumerate(pages): # TODO: set back all pages
        result_raw = chain.run(document_content=page,
                            output_template_json=OUTPUT_TEMPLATE_JSON,
                            types = METADATA["types"],
                            topics = METADATA["topics"],
                            statusOptions = METADATA["statusOptions"])
        raw_results += [result_raw]
        
        # Clean the result
        result_sliced=result_raw[result_raw.find("["):result_raw.rfind(']')+1]
        result_sliced=re.sub(' +', ' ', result_sliced)
        result_sliced=re.sub('\n', '', result_sliced)

        if result_sliced == "[]":
            pass
        else:
            result_tmp = json.loads(result_sliced)
            result_cleaned = []

            # Add metadata
            for j in range(len(result_tmp)):
                if (result_tmp[j]["issue_fr"] != "/" or result_tmp[j]["issue_nl"] != "/"):
                    result_tmp[j]["page"] = i + 1 
                    result_tmp[j]["filename"] = cloud_metadata["filename"]
                    result_tmp[j]["policy_level_fr"] = cloud_metadata["policy_level_fr"]
                    result_tmp[j]["policy_level_nl"] = cloud_metadata["policy_level_nl"]
                    result_tmp[j]["date_scraped"] = date_scraped
                    result_cleaned += [result_tmp[j]]

            results += result_cleaned
    
    return results, raw_results