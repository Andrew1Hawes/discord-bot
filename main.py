#bot client id: 661929485603569692
#bot token (KEEP PRIVATE): see token.txt
#permissions integer: 75840
#to add bot to server: https://discordapp.com/oauth2/authorize?client_id=<Bot_Client_ID>&scope=bot&permissions=0
#in documentation coroutine means use await!
import discord
import logging
from json import loads
from urllib import request

CMD_PREFIX = '!'
OPS = ("MrStewie64#9056")

logging.basicConfig()
client = discord.Client()
token = open("token.txt", "r").read()

@client.event #event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user: #ignore this bot's messages
        return
    
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if message.content.startswith(CMD_PREFIX):
        splitContent = message.content.split()
        cmd = splitContent[0][len(CMD_PREFIX):].lower()
        if cmd == "hi":
            await message.channel.send(f"Hi {message.author.name}!")
        elif cmd == "ip":
            # This line will connect to the website, read its contents
            # and parse the JSON output
            data = loads(request.urlopen("http://httpbin.org/ip").read())
            ip0 = data['origin'].split(",")[0]
            await message.channel.send(f"The public IP is: ```{ip0}```")
        elif cmd == "logout":
            if str(message.author) in OPS:
                await message.channel.send("Bravo Six, going dark.")
                await client.close()
                exit()
            else:
                message.channel.send(f"{message.author.name}, you don't have permission to run that.")

client.run(token)
