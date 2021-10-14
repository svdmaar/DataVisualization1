import requests

from operator import itemgetter

#url = "https://hacker-news.firebaseio.com/v0/item/9884165.json"
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

r = requests.get(url)

print("Status code: " + str(r.status_code))

submission_ids = r.json()

print("id count = " + str(len(submission_ids)))

submission_dicts = []
for submission_id in submission_ids[:10]:
    print(submission_id)
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json"
    submission_r = requests.get(url)
    response_dict = submission_r.json()
    #print(response_dict["title"])

    submission_dict = {
        "title": response_dict["title"],
        "comments": response_dict.get("descendants", 0)
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print("Title: " + submission_dict["title"])
    print("Comments: " + str(submission_dict["comments"]))
