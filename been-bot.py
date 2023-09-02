##been-bot

import discord 
import time
import random
import asyncio

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

#dict for all players
#dict for who all is gambling currently 
#add or subtract current gambling winnings and losses from all players dict 
players = {}
initGold = 1000
winners = {}
wager = ""
rolls = {}

startTime = time.localtime()
    
def writeToDict(dict, val, amount):
        dict[val] = amount 
    
def updateLosers(dict1, dict2, val1, val2, amount):
        dict1.update({val1: amount})
        
            

    
start_Time = time.monotonic()

@client.event
async def on_message(message):
    betters = {'Shirt': 1000}
    rolls = {'Shirt': 1000}
    
    if message.content == "!gamble help":
        
        message.channel.send("type !gamble(100 / 250 / 500 / 1000)")
        
    if message.content == "!gamble 100":
        
        wager = 100
        
        roll = random.randrange(1, wager, 1)
        
        message.channel.send("Press 1 to enter. 20 seconds.")
        
        def bet_Timer():
            if message.content.startswith("1"):
                betters[message.author] = wager
            client.wait_for('message', timeout=20.0, check="1")
        bet_Timer()
    
        for i in betters:
            roll 
            await message.channel.send(f"{betters[i]} rolled a {roll}.")
            rolls[i] = roll
        
        winnerName = max(rolls, key = rolls.get)
        
        max_roll = rolls[winnerName]
        
        pot = wager * len(betters)
        
        message.channel.send(f"{winnerName} wins with a roll of {max_roll}!")
        
        players[winnerName] += pot
        
        del betters[winnerName]
        
        for i in betters[i]:
            players[i] = (initGold - wager)
            
client.run("MTE0MTI5NzQwMjc2MzAzMDUzOQ.GpO_BA.bf6QFpOwvOW-tTchnPBcXp1VMSRZTOzyq67pOo")