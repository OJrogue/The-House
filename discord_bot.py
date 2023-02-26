import discord
from game import Game

# insert your bot token
token = ''

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

games = {}


@client.event
async def on_ready():
    print("Logged in as: {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user or message.author.id == 557628352828014614:
        return

    elif message.author.id not in games.keys():
        games[message.author.id] = Game()

    text = games[message.author.id].com(message.content)

    embedVar = discord.Embed(description=text)
    embedVar.set_author(name=message.author.name,
                        icon_url=message.author.avatar)

    await message.channel.send(embed=embedVar)

client.run(token)
