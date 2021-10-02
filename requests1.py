import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()

print(response_dict.keys())

print("Total repos: " + str(response_dict["total_count"]))

repo_dicts = response_dict["items"]
print("Repositories returned: " + str(len(repo_dicts)))

repo_dict = repo_dicts[0]
print("Keys: " + str(len(repo_dict)))
for key in sorted(repo_dict.keys()):
    print(key)

names = []
stars = []
for repo_dict in repo_dicts:
    print("Name: " + repo_dict["name"])
    print("Owner: " + repo_dict["owner"]["login"])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
