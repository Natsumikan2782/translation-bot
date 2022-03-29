import discord
from discord import Message
import json
import requests

with open('config.json', encoding='utf-8') as f:
        config = json.load(f)

client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print('\nLogged in as')
    print(client.user)
    print('------')
    await client.change_presence(activity=discord.Game("🤯RATTED-ALERT🤯"))
    
@client.event    
async def on_message(message: Message):
    
    if message.author.bot:
        return
    
    elif message.content.startswith("!trans"):
        args = message.content.split()
        req = f"https://script.google.com/macros/s/AKfycbzZtvOvf14TaMdRIYzocRcf3mktzGgXvlFvyczo/exec?text={' '.join(args[3:])}&source={args[1]}&target={args[2]}"
        date = requests.get(req).json()
        word = date["text"]
        
        embed = discord.Embed(title=f"{args[1]}➪{args[2]}", description="",color=0xa88dfa)
        embed.add_field(name="原文",value="``" + ' '.join(args[3:]) + "``",inline=False)
        embed.add_field(name="翻訳",value="``"+word+"``")
        embed.set_footer(text = "Powered by natsumi#7504")
        
        await message.channel.send(embed=embed)
    
TOKEN = config["token"]
client.run(TOKEN)    
