import tweepy

access_token = '1193375205424541697-AFjUxzOmuuOOnM0I2roXnuwrb4lT0c'
access_token_secret = '34WENDNHQrCZFjzmyAljXRPqwq04jCrZcYzCQ0Otc26oA'
consumer_key = '0UtEKJpGR8X4mUdyeWvvTlm8u'
consumer_secret = 'XQWxWYFqIlcwA7Odscj6NFZvUoJmefv6X8JZh83xVAWobQh11U'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret,access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
