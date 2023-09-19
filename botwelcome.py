import discord
import random
from io import BytesIO
from PIL import Image

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {.user}'.format(client))

@client.event
async def on_member_join(member):

    channel = client.get_channel(1019776265508638750)
    base_image = Image.open("greeting_template.png")
    avatar = await member.avatar_url_as(size=128).read()
    paste_image = Image.open(BytesIO(avatar)).resize((150, 150))
    base_image.paste(paste_image, (100, 100))
    greeting = f"Trào cậu {member.mention}! Nghỉ chân ở đây một lúc nhá."

    image_bytes = BytesIO()
    base_image.save(image_bytes, format="PNG")
    image_bytes.seek(0)
    await channel.send(greeting, file=discord.File(fp=image_bytes, filename="greeting.png"))

    emoji_list = [":Fc_mOop: ", ":Fc_mBlush: ", ":Fc_moke: ", ":Fc_mSmile: ", ":Fc_mMelon: ", ":Fc_mIKnowSomethingYouDont: ", ":Fc_FBlush: ", ":Fc_FUwU: "]
    decorated_emoji = random.choice(emoji_list)
    await channel.send(f"{decorated_emoji}")

client.run('MTA2ODczNTU1ODk1Mzc1MDU1MA.GReIcs.tEQV-S7xXgn8ab_g3_yW-A2odS2faorpQGHyiI') 
