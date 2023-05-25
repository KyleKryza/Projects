from urllib.request import Request, urlopen
import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import tasks
from etherscan import Etherscan
import json

client = discord.Client()
eth = Etherscan("YOUR KEY")


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    send.start()


@tasks.loop(seconds=30)
async def send():
    try:
        URL = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey="
        APIKEY = "YOUR KEY"
        response = requests.get(URL + APIKEY)
        payload = response.json()
        slow = str(payload['result']['SafeGasPrice'])
        avg = str(payload['result']['ProposeGasPrice'])
        fast = str(payload['result']['FastGasPrice'])
        status = slow + "/" + avg + "/" + fast
        await client.change_presence(activity=discord.Game(status))
    except:
        print("Error")


@send.before_loop
async def before():
    await client.wait_until_ready()


client.run('YOUR BOT KEY')