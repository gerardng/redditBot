import praw
import pdb
import re
import os
from config_bot import *

# Check that the file that contains our username exists
if not os.path.isfile("config_bot.py"):
    print "You must create a config file with your username and password."
    print "Please see config_skel.py"
    exit(1)

# Create a Reddit instance
user_agent = ("PyGer bot 0.1")
r = praw.Reddit(user_agent = user_agent)

# login
r.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("replied_heap.txt"):
    replied_heap = []
else:
    # Read file, split, remove last null
    with open("replied_heap.txt", "r") as f:
        replied_heap = f.read()
        replied_heap = replied_heap.split("\n")
        replied_heap = filter(None, replied_heap)

# Get values from subreddit
subreddit = r.get_subreddit(SUBREDDIT_NAME)
for submission in subreddit.get_hot(limit = 20):
    # print submission.title

    # If we haven't replied to this post before
    if submission.id not in replied_heap:

        # Do a case insensitive search
        if re.search(SUBMISSION_TITLE, submission.title, re.IGNORECASE):
            # Reply to the post
            submission.add_comment(REPLY_MESSAGE)
            print "Bot replying to : ", submission.title

            # Store the current id into our list
            replied_heap.append(submission.id)

# Write our updated list back to the file
with open("replied_heap.txt", "w") as f:
    for post_id in replied_heap:
        f.write(post_id + "\n")