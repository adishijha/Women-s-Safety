import tweepy

consumer_key='Given in twitter developer account'
consumer_secret='Given in twitter developer account'
access_token='Given in twitter developer account'
access_token_secret='Given in twitter developer account'

def OAuth():
    try:
        auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        return auth

    except Exception as e:
        return None
