##been-bot

import discord
import time
from random import random
import math


intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('420'):
        await message.channel.send('69')

client.run('MTE0MTI5NzQwMjc2MzAzMDUzOQ.GdVD9E.EDt8VGAjYprCSIeh2Hwr3H4ksGQwLnIGouBjfI')

@client.event


class gambling:
    #dict for all players
    #dict for who all is gambling currently 
    #add or subtract current gambling winnings and losses from all players dict 
    players = {}
    betters = {}
    gold = 1000
    winners = {}
    
    
    
    winner = ""
    loser = ""
    
    def writeToDict(dict, val, amount):
        dict[val] = amount 
    
    def updateDict(dict, val, amount):
        dict.update
            
            

    
    start_Time = time.gmtime()
    
    async def on_message(message):
        players = {}
        betters = {}
        roll = random.randrange(1, wager, 1)
        wager = ""
        startTime = time.localtime()
        endTime = time.localtime() 
        if message.content.startswith(f"!gamble {wager}"):
            await message.channel.send("Press 1 to enter. 20 seconds.")
            while ((startTime) < (startTime + 20)):
                endTime = endTime + 1
                if message.content.startswith("1"):
                    betters[message.author] = wager
            
            for i in betters:
                print(f"{betters[i]} rolled a {roll}.")
            
