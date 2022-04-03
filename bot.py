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
        embed1 = discord.Embed(title="翻訳中...", description="",color=0xa88dfa)
        embed1.set_footer(text = "Powered by natsumi#7504")
        msg = await message.channel.send(embed = embed1)
        
        try:
            args = message.content.split()
            key = config["api-key"]
            req = f"https://api-free.deepl.com/v2/translate?auth_key={key}&text={' '.join(args[3:])}&source_lang={args[1]}&target_lang={args[2]}"
            date = requests.get(req).json()
            word = date["translations"][0]["text"]
        
            embed2 = discord.Embed(title=f"{args[1]}➪{args[2]}", description="",color=0xa88dfa)
            embed2.add_field(name="原文",value="``" + ' '.join(args[3:]) + "``",inline=False)
            embed2.add_field(name="翻訳",value="``"+word+"``")
            embed2.set_footer(text = "Powered by natsumi#7504")
        
            await msg.edit(embed=embed2)
            
        except KeyError:
            embed = discord.Embed(title="翻訳に失敗しました、言語が不正です。", description="",color=0xa88dfa)
            embed.set_footer(text = "Powered by natsumi#7504")
            await msg.edit(embed=embed)
    
TOKEN = config["token"]
client.run(TOKEN)    
