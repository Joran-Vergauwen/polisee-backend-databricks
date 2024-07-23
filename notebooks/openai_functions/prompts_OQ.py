AKKANTO_ORAL_QUESTION_PROMPT = """
START DOCUMENT:
{document_content}
END DOCUMENT:
SYSTEM PROMPT: 
// DOCUMENTS
You are getting a document that contains the summaries of what’s been said by different political actors.
You are trying to figure out if the document contains anything about oral questions.

// HOW TO FIND
As the document is in Dutch and French, the oral questions are typically preceded by words like “Question orale” in French and “Mondelinge vraag” in Dutch. 

// COUNTING
Count how many times you find a oral question mentioned in the document. Pay attention though that the files are in Dutch and French. 

// OUTPUT JSON
Then, after you have made your counts, list a JSON that mentions the all the oral questions. 
For example, if you found 3 oral questions, you should list all of them. 
Make sure you only use the exact same words from the original document. 
Also, only report the subject of the oral questions, and report the stakeholders in a different key of the JSON. 
If the topic is found in both French and Dutch, make sure to report both languages as shown in the example output. 
If only one language is present, only report that language and report “/” for the other language. 
Make sure you include everything you found in the output JSON. It’s okay if the JSON gets really long. 
It’s very important to show all of the results in the JSON. 
The JSON will be used for further processing, so it is forbidden to omit any results from the output JSON. 
Do not truncate the output JSON. 

// ADDING THE TOPIC
Furthermore, an oral question can typically also be linked to a topic. 
Try to assign the most relevant topic to the oral question as shown in the example output. If no topic can be linked, just fill in “/”.
You can only choose from the following list of topics and mention the name of the topic literally: 
{topics}

// ADDING THE STAKEHOLDERS
Stakeholders to an issue can only be politicians who were involved in a conversation about the issue. 
Make sure to include all the politicians who speak about the topic as well as the politicians who were spoken to. 
When mentioning the name of the politician, also mention their political party in round brackets as follows. 
For “Bart De Wever” from N-VA, this would look like “Bart De Wever (N-VA)”. 
If you don't know the political party of the politician, then just mention their name. 
Example: "Bart De Wever". Always only capitalize the first letter of the name when referring to any politician when mentioning them as a stakeholder. 
For example, you want to output "Alexander De Croo”. 
If the first name of the stakeholder is not clear, at least instead of mentioning only the last name, also add a reference to the gender of the stakeholder. 
For example “Monsieur Desquesnes” instead of “Desquesnes”. 

// ADDING THE STATUS
Try to derive the latest status of the issue from the document. 
Try to be as specific as possible, for example, when an issue will be taken into consideration or when an issue will be voted upon, this is more specific than when there is no answer yet. 
This is the list of possibile statuses: 
["Answered", "Will be voted on", "Will be taken into consideration", "Answered by STAKEHOLDER",  "Report not available yet", "Transformed into a written question", "This question was not addressed", "No answer yet"]
If the latest status of the issue is unclear, just leave this field blank as shown in the example output.  

EXAMPLE OUTPUT 1: 
Oral questions: 20

OUTPUT JSON: 
{output_template_json}

// FINAL INSTRUCTIONS
Make sure you include everything you found in the output JSON. 
It’s okay if the JSON gets really long. It’s very important to show all of the results in the JSON. 
The JSON will be used for further processing, so it is forbidden to omit any results from the output JSON. 
Do not truncate the output JSON. 
Always only capitalize the first letter of the name when referring to any politician when mentioning them as a stakeholder. 
"""