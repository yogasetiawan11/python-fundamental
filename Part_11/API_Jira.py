""" You can get this code from Jira API Documentation web
Purpose of This code is to make a list all project in my Jira account"""
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

# You have to change this link with your Jira account's link
url = "https://yogasetiawan11.atlassian.net//rest/api/3/project"

# You have to change this email with yours 
# put your API token that you Get in Jira 
API_TOKEN = "Put your Jira API here"

auth = HTTPBasicAuth("yogasn@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# This is the default print statement of Jira
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)

name = output[0] ["name"]

print(name)