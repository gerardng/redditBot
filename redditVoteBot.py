import praw
import getpass

user_agent = ("GerardPy Bot 0.1")

instance = praw.Reddit(user_agent = user_agent)

#login function
def login_reddit():
	global user_name
	user_name = input('Username: ')
	user_password = getpass.getpass()
	try:
		print('Attempting to log in Reddit')
		instance.login(username = user_name, password = user_password)
		print('Reddit log in success')
		return 0
	except Exception:
		print('Error logging in')
		return 1

#search function
def vote(other_user_para, limit_para, up_para):
	other_user = instance.get_redditor(other_user_para)
	print('Raiding user')
	limit = int(input('How many comments to modify?'))
	print('Requesting user ',other_user_para,' comments')
	generator = other_user.get_comments(sort='new',time='all',limit=limit_para)
	for comment in generator:
		if up_para == 1:
			print('Up-voting Comment [  ',comment,'  ] .')
        	comment.upvote()
        	print('Done..')
        else:
        	print('Down-voting Comment [  ',comment,'  ] .')
        	comment.downvote()
        	print('Done..')

print('Reddit Upvote/Downvote Bot by Gerard N')
print('Dashboard')
while login_reddit():
	continue
other_user_para = input('Enter reddit username to modify: ')
limit_para = input('Enter the number of comments to modify: ')
up_para = input('Enter 1 to upvote otherwise enter 0 to downvote')
vote(other_user_para, limit_para, up_para)
