import discord 
from discord.ext import tasks
import twitter_tweets
import json_to_message


class MyClient(discord.Client):
    
    async def on_ready(self):
        twitter_tweets.main()
        channel = client.get_channel()
        print(channel)
        self.newTweets.start()
        

    @tasks.loop(seconds =1)
    async def newTweets(self):
        print('Made it to loop')
        
        message = json_to_message.extract()
        print(message)
        await channel.send(message)

   
        
       
    
        
    
client = MyClient()
client.run('')