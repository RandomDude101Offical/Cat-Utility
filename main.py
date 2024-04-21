# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import discord

import asyncio


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('cat'):
        await message.channel.send('Cat!', file=discord.File("pictures/blink.gif"))


    if message.content.startswith('dog'):
        await message.channel.send('not quite')
        await asyncio.sleep(0.4)
        await message.channel.send('wrong animal')

    if message.content.startswith('weather'):
        await message.channel.send('Todays weather in tallinn is -93 Degress per celsius')

  
num_servers = len(client.guilds)
num_users = len(set([member.id for guild in client.guilds for member in guild.members]))

async def update_presence():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'in {num_servers} servers with {num_users} cats'))
# Call the async function before client.run(token)
asyncio.run(update_presence())
    # Move the async function call after client.run(token)

try:
  token = os.getenv("TOKEN") or "" # for security reasons
  if token == "":
      raise Exception("Please add your token to the Secrets pane.")
  client.run(token)

  # Check the client object before calling the async function
  if client.is_ready():
      asyncio.run(update_presence())
except discord.HTTPException as e:
  if e.status == 429:
      print(
          "The Discord servers denied the connection for making too many requests"
      )
      print(
          "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
      )
  else:
      raise e
