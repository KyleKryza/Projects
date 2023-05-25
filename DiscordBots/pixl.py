import requests
import discord
from discord.ext import tasks
from discord.ext import commands

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    send.start()


@tasks.loop(seconds=60)
async def send():
    try:
        response = requests.get("http://sappytracker.xyz/data.json")
        payload = response.json()
        status = "${:,.4f}".format(float(payload['pixl_price']))
        await client.change_presence(activity=discord.Game(status))
    except:
        print("Error Occured")


@send.before_loop
async def before():
    await client.wait_until_ready()
    

client.run('YOUR BOT KEY')