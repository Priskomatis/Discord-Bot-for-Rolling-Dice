import discord  #imports the library of discord. Discord.py.
import os
import random
import asyncio
from discord.ext import commands
from keep_alive import keep_alive

client = discord.Client()  #This is part of the discord.py library

d6 = [1, 2, 3, 4, 5, 6]
d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def rollTheDice(numOfDice, dieType):
	if dieType == '$roll 1d6':
		x = numOfDice * random.choice(d6)
		return x
	elif dieType == '$roll 1d10':
		x = numOfDice * random.choice(d10)
		return x
	elif dieType == '$roll 1d20':
		x = numOfDice * random.choice(d20)
		return x


@client.event  #This is how we register an event to trigger the bot
async def on_ready():  #This event is called when a bot is being used
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(
        message):  #Discord library searches for these functions to trigger.
	if message.author == client.user:  #This author is the bot, if the msg comes from the bot we don't want to get a trigger reply
		return

	if message.content.startswith('$roll'):
		await message.channel.send(
		    "please type how many dice you want toll and the type of dice: ")

		msg = await client.wait_for('message')
		await message.channel.send('Your message was: ' + msg.content)

		if msg.content.contains('d20'):
			rollTheDice(msg.get)


keep_alive()
client.run(os.getenv('TOKEN'))
