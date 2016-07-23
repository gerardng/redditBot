import praw

user_agent = ("GerardPy Bot 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("squaredcircle")

for submission in subreddit.get_top(limit = 5):
    print "Title: ", submission.title
    print "Score: ", submission.score
    print "Ups: ", submission.ups
    print "Downs: ", submission.downs
    print "Test: ", submission.visited


    print "---------------------------------\n"