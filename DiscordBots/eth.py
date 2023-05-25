from urllib.request import Request, urlopen
import requests
import discord
from discord.ext import tasks

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    send.start()


@tasks.loop(seconds=60)
async def send():
    try:
        URL = "https://api.etherscan.io/api?module=stats&action=ethprice&apikey="
        APIKEY = "YOUR KEY"
        response = requests.get(URL + APIKEY)
        payload = response.json()
        status = "${:,.2f}".format(float(payload['result']['ethusd']))
        await client.change_presence(activity=discord.Game(status))
    except:
        print("Error Occured")


@send.before_loop
async def before():
    await client.wait_until_ready()


client.run('YOUR BOT KEY')