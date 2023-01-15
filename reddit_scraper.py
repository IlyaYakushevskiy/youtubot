import praw
import pandas as pd
import json

#praw.Reddit(check_for_async=False)
# Define user agent
user_agent = "data_scraper"

# Create an instance of reddit class
reddit = praw.Reddit(username="Dr-Selver_17",
                     password="Zizn-illuzija",
                     client_id="NKEnCOpEFtRxujDj4FDc0w",
                     client_secret="cLB9klH6VtUnODr8RM2vUleNVdChjA",
                     user_agent=user_agent,
                     check_for_async=False
)
#Create sub-reddit instance
subreddit_name = "AmItheAsshole"
subreddit = reddit.subreddit(subreddit_name)
parameter = 300



titles=[]
scores=[]
ids=[]
selftexts=[]

#while len(ids) <= parameter:
for submission in subreddit.top(limit = parameter):
    if len(submission.selftext) < 1100 and len(submission.selftext) > 600:
        
        titles.append(submission.title)
        scores.append(submission.score) #upvotes
        ids.append(submission.id)
        selftexts.append(submission.selftext)
    print(len(ids))

mydict = {}
f = open("reddit_scrape_res.txt", "w", encoding = "UTF-8")
with open("data_scraper_res.json", "w") as chlen:
        chlen.close()
for x in range(len(ids)):

    prompt={"prompt":titles[x]}
    output={"output":selftexts[x]}
    f.write(str(mydict))
    mydict.update(prompt)
    mydict.update(output)

    
    with open("data_scraper_res.json", "a") as outfile:
        json.dump(mydict, outfile)
        outfile.close()


print("Started file writing.")


f.close()
print("Completed with ", len(ids), "posts!")