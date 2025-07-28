import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# print(response.json())
'''Output will be a list of pull requests in JSON format.'''

# print(response)
'''The output will be "<Response [200]>'''