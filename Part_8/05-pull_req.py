import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

data = response.json()

for i in range(len(response.json())):
    print(data [i]["user"]["login"])