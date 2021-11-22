import praw
reddit = praw.Reddit('DEFAULT')
for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)