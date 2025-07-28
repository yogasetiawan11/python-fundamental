import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# in previous code we can only put on the browser and get the code from the GitHub API
# but now we can use the requests library to fetch the pull requests programmatically using python.
