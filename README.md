# reddit_delete_old
Delete your old reddit comments/posts, even those that won't show up in your post history

I created this script as a result of not being able to find an adequate solution.

Shreddit will only delete posts that show on your profile pages.

Extensions for Chrome, etc are the same.

This script requires PRAW: https://github.com/praw-dev/praw

I am not going to explain how to set up PRAW here, their docs cover it well.

NOTE: I am not a python coder by trade - I just whipped this up quick to do something.

I sourced my list of post id's using the google big-query dataset maintained by redditors here: 

https://bigquery.cloud.google.com/table/fh-bigquery:reddit_comments.2017_02?tab=details

And used the following query to pull my post/comment id's

SELECT id
FROM [fh-bigquery:reddit_comments.all]
WHERE author = 'YourActualUserNameCaseSensetive'

I then exported this csv and fed this ids.csv into the python script
