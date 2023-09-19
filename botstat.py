import discord
from discord.ext import commands, tasks
from itertools import cycle

TOKEN = "MTA2ODczNTU1ODk1Mzc1MDU1MA.GReIcs.tEQV-S7xXgn8ab_g3_yW-A2odS2faorpQGHyiI"

client = commands.Bot(command_prefix= "j", intents= discord.Intents.all())

trang_thai = ["Trang_thai_1","Trang_thai_2","Trang_thai_3","Trang_thai_4"]
bot_tt = cycle(trang_thai)
@tasks.loop(seconds= 5)
async def change_status():
    await client.change_presence(activity = discord.Game(next(bot_tt)))

@client.event
async def on_ready():
    print("Khoi dong bot!")
    print('Logged in as {0.user}'.format(client))
    change_status.start()

client.run(TOKEN)