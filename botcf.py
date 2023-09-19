import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot coinflip is running!")
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if (message.author == client.user):
        return

    if message.content.startswith('Fccf'):
        coinflip_info = {
                'heads': {
                    'name': 'Heads',
                    'emoji': '⭐',
                    'color': discord.Color.gold()
                },
                'tails': {
                    'name': 'Tails',
                    'emoji': '⚫',
                    'color': discord.Color.dark_grey()
                }
            }
        coin = random.choice(['heads', 'tails'])
        await message.channel.send(f'The coin landed on {coin}!')

        embed = discord.Embed(title='Coin Flip Result', color=coinflip_info[coin]['color'])
        embed.set_author(name=message.author.display_name)
        embed.add_field(name=coinflip_info[coin]['name'], value=f'{coinflip_info[coin]["emoji"]}', inline=True)
        embed.add_field(name='Result', value=f'You {"won" if coin == "heads" else "lost"}!', inline=True)
        await message.channel.send(embed=embed)

client.run('MTA2ODczNTU1ODk1Mzc1MDU1MA.GReIcs.tEQV-S7xXgn8ab_g3_yW-A2odS2faorpQGHyiI') 