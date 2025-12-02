import requests

def get_github_status():
    url="https://api.github.com"
    response=requests.get(url)
    return response.status_code

staus_code=get_github_status()
print("GitHub API Status Code:", staus_code)