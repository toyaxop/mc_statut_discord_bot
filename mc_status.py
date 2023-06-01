import discord
from mcstatus import JavaServer
import asyncio
from datetime import datetime

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)
status_channel = SET-CHANNEL-ID-HERE # Replace it with the ID of the channel where you want the messages to be sent.
ancient_status = None
new_status = None

async def check_server():
    global ancient_status
    global new_status
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        try:
            server = JavaServer.lookup("IP") # Change "IP" here, with your server's IP.
            status = server.status()
            new_status = True
        except:
            print("Server closed")
            new_status = False
        try:
            if ancient_status != new_status or ancient_status == None or new_status == None:
                ancient_status = new_status
                if ancient_status == True:
                    title = f"The server is now open :green_circle: [{current_time}]"
                    color = 0x09ff00
                else:
                    title = f"The server is now closed :red_circle: [{current_time}]"
                    color = 0xff0000
                embed = discord.Embed(title=title, url="https://mcsrvstat.us/server/IP", description="The status may not be accurate. Please refer to https://mcsrvstat.us/server/IP for a more accurate source.\nBot developed by Toya#1234", color=color) # Replace the IP in "https://mcsrvstat.us/server/IP" by your server's IP.
                await client.get_channel(status_channel).send(embed=embed)
        except:
            ancient_status = new_status
            if ancient_status == True:
                title = f"The server is now open :green_circle: [{current_time}]"
                color = 0x09ff00
            else:
                title = f"The server is now closed :red_circle: [{current_time}]"
                color = 0xff0000
            embed = discord.Embed(title=title, url="https://mcsrvstat.us/server/IP", description="The status may not be accurate. Please refer to https://mcsrvstat.us/server/IP for a more accurate source.\nBot developed by Toya#1234", color=color) # Replace the IP in "https://mcsrvstat.us/server/IP" by your server's IP.
            await client.get_channel(status_channel).send(embed=embed)

        await asyncio.sleep(30)

@client.event
async def on_ready():
    print("Connected as {0.user}".format(client))
    await check_server()
        
client.run("TOKEN")
# I know this code sometimes sent fake status change, but it works perfectly to find out if your server has crashed.
