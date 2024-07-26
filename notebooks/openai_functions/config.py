METADATA = {
    "topics": ["Renewable Energy", "Wind Energy", "Offshore", "Aviation and Defense", "Energy and Heating", "Women's Health", "Tobacco and Smoking", "Environmental Issues", "Social Media and Online Platforms", "Banking and Finance", "Cardiovascular Health", "Chronic Diseases", "Cancer and Oncology", "Rare Diseases and Specialized Treatments", "Ophthalmology", "Healthcare System and Financing", "Pharmaceutical Industry and Regulation", "Mental Health and Neurology", "Blood Disorders and Hematology", "Transplantation and Immunology", "Vaccines and Infectious Diseases", "End-of-Life Care", "Public Health and Prevention", "Patient Care and Organizations", "Over-the-Counter Medications", "Drug Supply and Regulation", "Education"],
    "statusOptions": ["Answered", "Will be voted on", 
                      "Will be taken into consideration", "Answered by STAKEHOLDER", 
                      "Report not available yet", "Transformed into a written question",
                      "This question was not addressed", "No answer yet"],
    "types": ["Law Proposal", "Vote on Motions", "Oral Question", "Suggestion", "Joined Oral Questions", "Written Question", "Hearing"],
    "policy_levels": {
        "Kamer_Chambre": {
            "fr": "La Chambre",
            "nl": "De Kamer"
        },
        "VlaamsParlement_ParlementFlamand": {
            "fr": "Parlement De Flandres",
            "nl": "Vlaams Parlement",
        },
        "WaalsParlement_ParlementDeWallonie": {
            "fr": "Parlement De Wallonie",
            "nl": "Waals Parlement",
        },
        "BrusselsParlement_ParlementDeBruxelles": {
            "fr": "Parlement De Bruxelles",
            "nl": "Brussels Parlement",
        },
        "FWBParlement_ParlementFWB": {
            "fr": "Parlement de la Fédération Wallonie Bruxelles",
            "nl": "Parlement van de Federatie Wallonië-Brussel",
        },
        "Senaat_Senat": {
            "fr": "Le Senat",
            "nl": "De Senaat",
        }
    }
    }

def create_output_template_json(type):
    output = [{
        "issue_fr": f"{type} in French",
        "issue_nl": "/",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": "/",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": "/",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": "/",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "/",
    },
    {
        "issue_fr": "/",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4"],
        "status": "/",
    },
    {
        "issue_fr": f"{type} in French",
        "issue_nl": f"{type} in Dutch",
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    ]

    return output

OUTPUT_TEMPLATE_JSON = [
    {
        "topic": "Topic you found in the data",
        "type": "Type of event you found in the data",
        "issue_fr": "Issue in French",
        "issue_nl": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Will be taken into consideration",
    }, 
    {
        "topic": "Topic you found in the data",
        "type": "Type of event you found in the data",
        "issue_fr": "Issue in French",
        "issue_nl": "Issue in Dutch",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "",
    }, 
    {
        "topic": "Banking Services",
        "type": "Oral Question",
        "issue_fr": "/",
        "issue_nl": "Issue in Dutch",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Will be voted on",
    },
    {
        "topic": "Banking Services",
        "type": "Vote on motions",
        "issue_fr": ["Issue in French 1", "Issue in French 2", "Issue in French 3"],
        "issue_nl": ["Issue in Dutch 1", "Issue in Dutch 2", "Issue in Dutch 3"],
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "",
    }
]


AKKANTO_GPT_PROMPT_TEMPLATE = """

SYSTEM PROMPT: 
You are an intelligent machine that analyzes governmental texts for a company called Akkanto. 
They are trying to get information of potential changes, called 'issues', in legislation that can have an impact on the business of their clients. 
Use the given instructions and the document below to create your answer. 

// Topics
The company would like to know anything that relates to one or more of the following list of topics. 
Treat each topic individually and check whether something is mentioned that could relate to them in the provided document. 
This is the list of topics:
{topics}
List all issues for the same topic if you find multiple issues for that topic. 
List all issues that could relate to the topic even when the topic itself is not specifically mentioned. 
Include all issues that could relate to the topic in the final output, even when it is unclear if there is a direct impact. 
Make sure that you catch all issues that can have an effect on the topic. 
Also make sure that the 'issues' field only contains sentences that are literally in the provided document. 

// Events
Furthermore, the 'issues' are are also typically of a certain type. The following list sums up all the potential types: 
{types}

// Stakeholders
Stakeholders to an issue can only be politicians who were involved in a conversation about the issue. 
Make sure to include all the politicians who speak about the topic as well as the politicians who were spoken to. 
When mentioning the name of the politician, also mention their political party in round brackets as follows. 
For 'Bart De Wever' from N-VA, this would look like 'Bart De Wever (N-VA)'.
If you don't know the political party of the politician, then just mention their name. Example: "Bart De Wever"
Always use initcap to refer to any politician. For example, you want to output "Alexander De Croo" instead of "Alexander DE CROO". 

// Languages
If you find the same issue in Dutch and French, then report the issue in both languages as shown in the example output. 
Make sure to only use the literal words that have been mentioned in the document. 
If you find the issue for only 1 language, then report the issue for that language and report '/' for the other language. 
For example, if you only find the issue in Dutch, then report the issue in Dutch and report '/' for French. 

// Status
Try to derive the latest status of the issue from the document. 
Try to be as specific as possible, for example, when an issue will be taken into consideration or when an issue will be voted upon, 
this is more specific than when there is no answer yet. 
This is the list of possibile statuses: 
{statusOptions}
If the latest status of the issue is unclear, just leave this field blank as shown in the example output.  

### START DOCUMENT ###
{document_content}
### END DOCUMENT ###

You can find some further instructions down below to make your answer. 
First of all, your answers should be a list of JSONS, with every new topic having a new element in the list. 
This is a template of how the output should look like. 
{output_template_json}
FINAL INSTRUCTIONS:

// EXHAUSTIVE
Look for any issues that are relevant for the topics from the list. 
Treat each topic individually and check whether something is mentioned that could be related to these topics. 
Check each topic one by one.  
Make use of all information above and the provided document to formulate your answer. 

// OUTPUT FORMAT
Make sure your answer is in the same format as the examples. 

// Language
For the issue field, always quote directly from the file in the original language. 
If the issue was mentioned in French in the file, answer with those exact same words in French. 
If the issue was mentioned in Dutch in the file, answer with those exact same words in Dutch. 
If you find the issue in both French and Dutch, then report both languages as shown in the examples above. 
Pay close attention to put the Dutch formulation of the issue in the issue_nl field and the French formulation in the issue_fr field.

// REASONING & INDIVIDUAL APPROACH
Make sure to treat each keyword individually and report any issue that might relate to them. 
Include your reasoning about each topic in the output before reporting the final JSON output. 
Treat each topic individually. This means you should also include your reasoning about each topic individually. 
Every potential link in the document to any of the issues should be reported. 
If there can be any link between the topic and the text in the provided documents, it should be mentioned. 

// FINAL OUTPUT
After providing your reasoning, end your output by writing: "FINAL OUTPUT:" and then provide the JSON.
Include all issues that could relate to the topic in the final output, even when it is unclear if there is a direct impact. 
If the same issue is found for multiple topics, only report it for the best fitting topic to avoid duplicates. 
Always use double quotes when creating keys and values for the JSON.
"""
