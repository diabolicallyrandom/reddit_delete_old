#!/usr/bin/python

# Yes, really shitty code, really shitty error handling just to handle
# 403 and 404 errors for already deleted comments, and/or link posts, etc

import praw
import time
import csv
import random

reddit = praw.Reddit('default', user_agent='my_reddit_deleter_username')

with open('/mnt/Path/To/File/ids.csv', 'r') as f:
	reader = csv.reader(f)
	my_list = list(reader)

random_list = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
		'Nunc varius velit a ipsum congue mollis.',
		'Ut luctus, ligula iaculis euismod vestibulum, urna lorem volutpat nisi, id eleifend metus nisi vitae diam.',
		'Pellentesque molestie mi sapien, dictum venenatis est interdum ac.',
		'Nunc a massa eleifend, porta libero nec, semper augue.',
		'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.',
		'Donec facilisis, dolor pharetra molestie laoreet, magna odio posuere sapien, et egestas purus libero vel enim.']

for comment_id in my_list:
	print 'Editing Comment ' + str(comment_id[0]) + '...'
	try:
		reddit.comment(str(comment_id[0])).edit(str(random.choice(random_list)))
	except:
		print 'Cant Edit.'
		pass
	time.sleep(1)
	print 'Deleting Comment ' + str(comment_id[0]) + '...'
	try:
		reddit.comment(str(comment_id[0])).delete()
	except:
		print 'Cant Delete.'
		pass
	time.sleep(1)
	print 'Done!'
