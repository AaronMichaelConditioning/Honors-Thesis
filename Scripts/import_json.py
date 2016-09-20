from __future__ import division
import json
import pandas as pd
import matplotlib.pyplot as plt
import tweepy

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)
tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

# print tweets['text']
# print tweets['lang']


numEn = 0
numEs = 0
numEt = 0
numFr = 0
numUnd = 0
numOther = 0
numTweets = len(tweets_data)

def calcPercentage(num, numTweets):
	percent = num/numTweets*100
	return percent

"""
for i in len(tweets_data):
	if tweets['lang'] == 'en':
		numEn = numEn + 1
	if tweets['lang'] == 'es':
		numEs = numEs + 1
	if tweets['lang'] == 'et':
		numEt = numEt + 1
	if tweets['lang'] == 'fr':
		numFr = numFr + 1
	if tweets['lang'] == 'und':
		numUnd = numUnd + 1
"""

for index, row in tweets.iterrows():
	if row['lang'] == 'en':
		numEn = numEn + 1
	elif row['lang'] == 'es':
		numEs = numEs + 1
	elif row['lang'] == 'et':
		numEt = numEt + 1
	elif row['lang'] == 'fr':
		numFr = numFr + 1
	elif row['lang'] == 'und':
		numUnd = numUnd + 1
	else:
		numOther = numOther + 1

percentEn = calcPercentage(numEn, numTweets)
percentEs = calcPercentage(numEs, numTweets)
percentEt = calcPercentage(numEt, numTweets)
percentFr = calcPercentage(numFr, numTweets)
percentUnd = calcPercentage(numUnd, numTweets)
percentOther = calcPercentage(numOther, numTweets)


print "Percent of Tweets in English: ", percentEn,"%"
print "Percent of Tweets in Spanish: ", percentEs,"%"
print "Percent of Tweets in Estonian: ", percentEt,"%"
print "Percent of Tweets in French: ", percentFr,"%"
print "Percent of Tweets in Undetermined: ", percentUnd,"%"
print "Percent of Tweets in Other: ", percentOther,"%"



tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')



	
