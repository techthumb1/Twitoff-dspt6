import tweepy
import os
from dotenv import load_dotenv


load_dotenv()

TWITTER_API_KEY = os.getenv("mmpIITrs6V5wUEvOEvtl6tZrE")
TWITTER_API_SECRET = os.getenv("blHXcQdMYjCaAVvgtLqG7W2VOo87uBHXuF2xpbho4lOts81BT3")
TWITTER_ACCESS_TOKEN = os.getenv("3079411932-jCLGJWhKZ3MnaYOxhxASQjAFib2ziHnecu5wobi")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("E3Krap22K0MTWZ1VBuJxBiPVHqgVg0ygYsUtuOvCuBuZ0")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", type(auth))

api = tweepy.API(auth)
print("API CLIENT", type(api))

user = api.get_user("techthumb1")
print(type(user))

breakpoint()


#def twitter_api():
#    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
#    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
#    print("AUTH", auth)
#    api = tweepy.API(auth)
#    print("API", api)
#    #print(dir(api))
#    return api
#
#if __name__ == "__main__":
#
#    api = twitter_api()
#    user = api.get_user("elonmusk")
#    print("USER", user)
#    print(user.screen_name)
#    print(user.name)
#    print(user.followers_count)

    #breakpoint()

    #public_tweets = api.home_timeline()
    #
    #for tweet in public_tweets:
    #    print(type(tweet)) #> <class 'tweepy.models.Status'>
    #    #print(dir(tweet))
    #    print(tweet.text)
    #    print("-------------")
