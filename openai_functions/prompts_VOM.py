AKKANTO_VOTE_ON_MOTIONS_PROMPT = """
START DOCUMENT:
{document_content}
END DOCUMENT:
SYSTEM PROMPT: 
// DOCUMENTS
You are getting a document that contains the summaries of what’s been said by different political actors. 
You are trying to figure out if the document contains anything about votes on motion.

// HOW TO FIND
As the document is in Dutch and French, the votes on motion are typically preceded by words like “Motions”, “Votes de motion” and “Projets de motion” in French and “Moties” in Dutch. 

// COUNTING
Count how many times you find a vote on motion mentioned in the document. Pay attention though that the files are in Dutch and French. 

// OUTPUT JSON
Then, after you have made your counts, list a JSON that mentions the key context of the all the votes on motion. 
Make sure you use the exact same words from the original document. 
Also, only mention the context of the motion in the “fr” and “nl” fields. 
Keep all references to stakeholders out when mentioning the subject of the motion in the “fr” and “nl” fields. 
If the motion is about multiple different subjects, mention the context of these different subjects in a list as shown in the example. 
If the topic is found in both French and Dutch, make sure to report both languages as shown in the example output. 
If only one language is present, only report that language and report “/” for the other language. 
Make sure you include everything you found in the output JSON. It’s okay if the JSON gets really long. 
It’s very important to show all of the results in the JSON. 
The JSON will be used for further processing, so it is forbidden to omit any results from the output JSON. 
Do not truncate the output JSON. 

// MENTIONING MOTIONS
When mentioning the motion, only report the content of the motion. 
If the motion is about multiple different things, mention these different things in a list as shown in the example output. 

// ADDING THE TOPIC
Furthermore, an vote on motion can typically also be linked to a topic. 
Try to assign the most relevant topic to the vote on motion as shown in the example output. 
If no topic can be linked, just fill in “/”. You can only choose from the following list of topics and mention the name of the topic literally: 
{topics}

// ADDING THE STAKEHOLDERS
Stakeholders to an issue can only be politicians who were involved in a conversation about the issue. 
Make sure to include all the politicians who speak about the topic as well as the politicians who were spoken to. 
When mentioning the name of the politician, also mention their political party in round brackets as follows. 
For “Bart De Wever” from N-VA, this would look like “Bart De Wever (N-VA)”. 
If you don't know the political party of the politician, then just mention their name. Example: "Bart De Wever". 
Always only capitalize the first letter of the name when referring to any politician when mentioning them as a stakeholder. 
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
Votes on motion: 20

OUTPUT JSON: 
{output_template_json}

// FINAL INSTRUCTIONS
// GENERAL
Make sure you include everything you found in the output JSON. It’s okay if the JSON gets really long. 
It’s very important to show all of the results in the JSON. 
The JSON will be used for further processing, so it is forbidden to omit any results from the output JSON. 
Do not truncate the output JSON. 

// MENTIONING STAKEHOLDERS 
Always only capitalize the first letter of the name when referring to any politician when mentioning them as a stakeholder. 

// MENTIONING MOTIONS
Make sure you use the exact same words from the original document. 
Also, only mention the context of the motion in the “fr” and “nl” fields. 
Keep all references to stakeholders out when mentioning the context of the motion in the “fr” and “nl” fields. 
If the motion is about multiple different subjects, mention the context of these different subjects in a list as shown in the example. 
Use only words from the original document when mentioning the motions.
"""

OUTPUT_TEMPLATE_JSON_VOTE_ON_MOTION = [
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["/"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["/"],
        "issue_nl": ["Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch"],
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["/"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["/"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch"],
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch"],
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "/",
    },
    {
        "issue_fr": ["/", "/", "/"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4", "Stakeholder 5"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch"],
        "topic": "/",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3", "Stakeholder 4"],
        "status": "/",
    },
    {
        "issue_fr": ["Vote on motion in French", "Vote on motion in French", "Vote on motion in French"],
        "issue_nl": ["Vote on motion in Dutch", "Vote on motion in Dutch", "Vote on motion in Dutch"],
        "topic": "Best fitting topic",
        "stakeholders": ["Stakeholder 1", "Stakeholder 2", "Stakeholder 3"],
        "status": "Latest status",
    },
]