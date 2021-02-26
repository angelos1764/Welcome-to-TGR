import discord
import os
from discord.utils import get

client = discord.Client()

buyer_words = ["m+", "mythic", "mythic+", "buy", "price", "much", "cn", "castle", "raid", "pvp", "boost", "looking", "lf", "key", "cost", "heroic", "carry", "torghast"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!buyer" and message.channel.id == 720185655858298902:
        role = get(message.guild.roles, id=692435065359040602)
        await message.author.add_roles(role)
    if any(word in message.content for word in buyer_words) and message.channel.id == 689513902211334182:
        await message.channel.send(message.author.mention)
        await message.channel.send('Thank you for reaching out to TGR for your boosting needs. An advertiser will DM you shortly.')
        channel = client.get_channel(690239876805034122)
        await channel.send('@here Please check <#689513902211334182>')

client.run(os.getenv('TOKEN'))