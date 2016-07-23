import praw
import sys

user_agent = ("GerardPy Bot 0.1")
r = praw.Reddit(user_agent = user_agent)
start = 1

#Input function
def get_user_input():
	subr = raw_input('Enter subreddit to inspect: ')
	#User wants to exit program
	if subr in("exit", "Exit", "close", "Close"):
		print('Closing program...')
		sys.exit(0)

	limitr = input('Enter number of posts to look at: ')

	subreddit = r.get_subreddit(subr)
	for submission in subreddit.get_top(limit = limitr):
		print "Title: ", submission.title
		print "Score: ", submission.score
		print "Ups: ", submission.ups
		print "Downs: ", submission.downs
		print "---------------------------------\n"


print('\nSubreddit Stats View by Gerard N')
print('--type exit to close the program')
while start:
	get_user_input()
