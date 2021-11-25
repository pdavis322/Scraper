import praw
import pickle
from psaw import PushshiftAPI
from textblob import TextBlob
import nltk.data
from flair.models import TextClassifier
from flair.data import Sentence
# Include praw.ini file for this to work without having client id/secret and user agent: see https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit('DEFAULT')
api = PushshiftAPI(reddit)
# Use tuple of names as key (e.g. rtz, arteezy)
# (num_positive, num_negative)
#players = {'rtz': [0, 0], 'arteezy': [0, 0], 'fly': [0, 0], 'bulba': [0, 0], 'ana': [0, 0], 'jerax': [0, 0], 'yatoro': [0, 0], 'mason': [0, 0], 'gorgc': [0, 0], 'gorp': [0, 0], 'ceb': [0, 0], 'ppd': [0, 0], 'alliance': [0, 0], 'loda': [0, 0]}
players = {'amazon': [0, 0], 'microsoft': [0, 0], 'google': [0, 0], 'apple': [0, 0], 'netflix': [0, 0], 'facebook': [0, 0], 'uber': [0, 0], 'lyft': [0, 0], 'bloomberg': [0, 0]}

#results = api.search_submissions(after=1606085388, q='|'.join(list(players.keys())), subreddit='dota2')
#results2 = list(api.search_comments(after=1596251889, q='|'.join(list(players.keys())), subreddit='dota2'))
results = []
results = list(api.search_comments(after=1596251889, q='|'.join(list(players.keys())), subreddit='csmajors'))
# First time only
with open('companies.pkl', 'wb') as f:
    pickle.dump(results, f)

# with open('dota2.pkl', 'rb') as f:
#     results = pickle.load(f)


# for s in results:
#     for c in players:
#         if c in s.selftext.lower():
#             players[c] += TextBlob(s.selftext).sentiment.polarity
#     count += 1

tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
# TextBlob
for s in results:
    for i, sentence in enumerate(tokenizer.tokenize(s.body)):
        for c in players:
            if c in sentence.lower():
                tb = TextBlob(sentence).sentiment
                if tb.subjectivity > 0.5:
                    players[c][0] += tb.polarity
                    players[c][1] += 1

for c in players:
    print(f'{c}: {players[c][0] / players[c][1] if players[c][1] > 0 else 0}')

# Flair
# classifier = TextClassifier.load('en-sentiment')
# for s in results:
#     for i, sentence in enumerate(tokenizer.tokenize(s.body)):
#         for c in players:
#             if c in s.body.lower():
#                 sentence = Sentence(s.body)
#                 classifier.predict(sentence)
#                 if sentence.labels[0].value == 'POSITIVE':
#                     players[c][0] += 1
#                 else:
#                     players[c][1] += 1

# for c in players:
#     print(f'{c}: {players[c][0] / (players[c][0] + players[c][1]) if (players[c][0] + players[c][1]) > 0 else 0}')