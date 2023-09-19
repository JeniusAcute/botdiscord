import discord
from discord.ext import commands
import random

#=====================
TOKEN = 'MTA2ODczNTU1ODk1Mzc1MDU1MA.GReIcs.tEQV-S7xXgn8ab_g3_yW-A2odS2faorpQGHyiI'

#=====================
client = commands.Bot(command_prefix="j", intents = discord.Intents.all())

#=====================
@client.event
async def on_ready():
    print("Bot normal is running!")
    print('Logged in as {0.user}'.format(client))

#=====================
@client.command()
async def ping(tin_nhan):
    do_tre = round(client.latency * 1000)
    await tin_nhan.send(f"Pong {do_tre} ms!")

#=====================
@client.command(aliases = ["8b","8ball","m8b"])
async def m8ball(ctx,*,question):
    with open("C:\\Users\\manhl\\Desktop\\Python_bot\\b_4_use_python\\tra_loi.txt", "r") as f:
        traloi_ngaunhien = f.readlines()
        traloi = random.choice(traloi_ngaunhien)
    await ctx.send(traloi)

#=====================
@client.command(aliases = ["xinchao","chao"])
async def hello(tin_nhan):
    await tin_nhan.send("Hello World!!!")

#=====================
@client.command(aliases = ["cf"])
async def coinflip(tin_nhan,*,mat):
    cfinfo = ["Head","Tail"]                #tep ket qua de random
    coin =  random.choice(cfinfo)           #coin la ket qua ngau nhien
    if ((coin == "Head") and ((mat == "h") or (mat == "head"))):
        await tin_nhan.send(coin + " \r\nYou win")
    elif ((coin == "Tail") and ((mat == "t") or (mat == "tail"))):
        await tin_nhan.send(coin + "\r\nYou win")
    else:
        await tin_nhan.send(coin + "\r\nYou lose")
        
#=====================
#@client.event
#async def on_message(tin_nhan):
#    if tin_nhan.author == client.user:
#        return
#    if tin_nhan.content.startswith("f"):
#        await tin_nhan.channel.send("Phan hoi")
#=====================

client.run(TOKEN)