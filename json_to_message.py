import json
import discord_message

tweet_str=[]

def json_message(json_string):

    enter_tweet = json.loads(json_string)
    exit_tweet =  'https://twitter.com/twitter/status/'+enter_tweet['data']['id'] +'\n'

    # This is for the discord_message_test run
    # tweet_str.append(exit_tweet) 
    # ----------------------------------------

    # This is for the twitter_tweets run
    discord_message.run_bot(exit_tweet) 
    

def extract():
    print("ARGHGGGG"+ " "+ len(tweet_str))
    if len(tweet_str) >=1:
        tweet= tweet_str.pop(0)
        return tweet 

    
    
    

     
   