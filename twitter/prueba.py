import tweepy
import json

access_token = '1193375205424541697-AFjUxzOmuuOOnM0I2roXnuwrb4lT0c'
access_token_secret = '34WENDNHQrCZFjzmyAljXRPqwq04jCrZcYzCQ0Otc26oA'
consumer_key = '0UtEKJpGR8X4mUdyeWvvTlm8u'
consumer_secret = 'XQWxWYFqIlcwA7Odscj6NFZvUoJmefv6X8JZh83xVAWobQh11U'

auth = tweepy.OAuthHandler(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )

api = tweepy.API(auth)

"""
# datos de mi cuenta
data = api.verify_credentials()
print(json.dumps(data._json, indent=4))
"""

"""
# Obtener información de otro usuario
data = api.get_user(screen_name="riosmauricio")
print(json.dumps(data._json, indent=2))
"""

"""
# Obtener los seguidores de un usuario utilizando cursor
data=api.get_followers(screen_name="nike")
for user in tweepy.Cursor(api.get_followers, screen_name="nike").items(50):
    print(json.dumps(user._json, indent=2))
"""

"""
# Obtener las personas que sigue un usuario utilizando cursor
data=api.get_friends(screen_name="nike")
for user in tweepy.Cursor(api.get_friends, screen_name="nike").items(50):
    print(json.dumps(user._json, indent=2))
"""

"""
# Obtener un timeline (tweets que hizo una personas) de un usuario
for tweet in tweepy.Cursor(api.user_timeline,screen_name="riosmauricio",tweet_mode="extended").items(20):
    print(json.dumps(tweet._json, indent=2))
"""

"""
# Buscar tweets
for tweet in tweepy.Cursor(api.search_tweets, q="censo2023", tweet_mode="extended").items(20):
    #print(json.dumps(tweet._json, indent=2,ensure_ascii=False))
    print(tweet.full_text)
    print()
"""





