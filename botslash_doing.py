import discord
from discord.ext import commands
from discord import app_commands
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
    try: 
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

#=====================
@client.tree.command(name = "xinchao")
async def hello(tuong_tac: discord.Integration):
    await tuong_tac.response.send_message(f"Xin chao {tuong_tac.user.mention}! Day la lenh SLASH")

#=====================
@client.tree.command(name = "noi")
@app_commands.describe(noi_gi_do = "What should i say?")        #noi_gi_do o tren duoi phai giong nhau
async def say(tuong_tac: discord.Integration, noi_gi_do: str):
    await tuong_tac.response.send_message(f"{tuong_tac.user.name} noi: {noi_gi_do}")

#=====================
@client.tree.command(name = "coinflip")                         #ten hien thi cua lenh slash
@app_commands.describe(mat_xu = "chon mat cho dong xu")         #giai thich gia tri
async def cf(tuong_tac: discord.Integration, mat_xu: str):      #tuong_tac phan can xu ly, mat_xu de xet dieu kien
    cfinfo = ["Head","Tail"]                                    #tep ket qua de random
    coin =  random.choice(cfinfo)                               #coin la ket qua ngau nhien
    #await tuong_tac.response.send_message(f"Ban chon {mat_xu}")                 
    if ((coin == "Head") and ((mat_xu == "h") or (mat_xu == "head"))):
        #await tuong_tac.response.send_message(coin + " \r\nYou win")                           #lenh nay van chay duoc
        await tuong_tac.response.send_message(f"Ban chon {mat_xu} \r\n{coin} \r\nYou win")
    elif ((coin == "Tail") and ((mat_xu == "t") or (mat_xu == "tail"))):
        #await tuong_tac.response.send_message(coin + "\r\nYou win")
        await tuong_tac.response.send_message(f"Ban chon {mat_xu} \r\n{coin}\r\nYou win")
    else:
        #await tuong_tac.response.send_message(coin + "\r\nYou lose")
        await tuong_tac.response.send_message(f"Ban chon {mat_xu} \r\n{coin}\r\nYou lose")

#=====================
#@client.tree.command(name = "ping")
#async def ping(tuong_tac: discord.Integration):
#    do_tre = round(tuong_tac.latency * 1000)
#    await tuong_tac.ressponse.send_message(f"Pong {do_tre} ms!")
#=====================

client.run(TOKEN)