from typing import Text
import praw
import requests
from psaw import PushshiftAPI
from flair.models import TextClassifier
from flair.data import Sentence
# Include praw.ini file for this to work without having client id/secret and user agent: see https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit('DEFAULT')
api = PushshiftAPI(reddit)
# Use tuple of names as key (e.g. rtz, arteezy)
companies = {'rtz': 0, 'arteezy': 0, 'fly': 0, 'bulba': 0, 'ana': 0, 'jerax': 0, 'yatoro': 0, 'mason': 0, 'gorgc': 0, 'gorp': 0, 'ceb': 0, 'ppd': 0, 'alliance': 0, 'loda': 0}
count = 0
sentence = Sentence('GOOD ONE LOL')
classifier = TextClassifier.load('en-sentiment')
classifier.predict(sentence)
print(sentence.labels[0].value)
print(sentence.labels[0].score)
#amazon = api.search_submissions(after=1606085388, q='|'.join(list(companies.keys())), subreddit='dota2')
#amazon = list(api.search_comments(after=1606085388, q='|'.join(list(companies.keys())), subreddit='dota2'))
# for s in amazon:
#     for c in companies:
#         if c in s.selftext.lower():
#             companies[c] += TextBlob(s.selftext).sentiment.polarity
#     count += 1
# for s in amazon:
#     for c in companies:
#         if c in s.body.lower():
#             companies[c] += TextBlob(s.body).sentiment.polarity
#     count += 1

# for c in companies:
#     print(f'{c}: {companies[c] / count}')