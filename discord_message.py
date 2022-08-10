import discord 
import twitter_tweets

def run_bot(message):
    class MyClient(discord.Client):

        async def on_ready(self):
            # Ill provide channel
            channel = client.get_channel() 
            await channel.send(message)
            await client.close()
            # twitter_tweets.main() leave this commented out
            
        
    client = MyClient()
    # Discord Token
    client.run('') 

        
        


        
