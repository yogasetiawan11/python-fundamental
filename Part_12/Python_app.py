import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# I make some Changes here from "/" to createJIRA
@app.route("/createJIRA", methods=['POST'])
def createJIRA():

    url = "https://your-domain.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("email@example.com", "<api_token>")

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first JIRA Ticket.",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10035"
        },
        "project": {
        "key": "YOGA"
        # Change id to key 
        },
        "summary": "First JIRA with Python",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    # intstead of print statement, we use 'return' because this is a API we cannot use Print statement
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0', port=5000)

