import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA2ODczNTU1ODk1Mzc1MDU1MA.GReIcs.tEQV-S7xXgn8ab_g3_yW-A2odS2faorpQGHyiI')