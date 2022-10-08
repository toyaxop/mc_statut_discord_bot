import discord
from mcstatus import JavaServer
from time import sleep
from datetime import datetime


default_intents = discord.Intents.default()
default_intents.members = True  # U need to activate intents in parameters of bots.
client = discord.Client(intents=default_intents)
status_channel = <Channel where the message while be send>
refresh_time = 300 # Refresh time u can change it

@client.event
async def on_ready():
    print("Logged as {0.user}. Code by Toya.Xo".format(client))
    server = JavaServer.lookup("<Your server adress>")
    while True:
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            # 'status' est supporté par tous les serveurs minecraft au dessus de la 1.7
            status = server.status()
            await client.get_channel(status_channel).send(f"Server : ON 🟩\n {status.players.online} players connected```") # Remove ``` if you don't want a blocky text.
        except:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            await client.get_channel(status_channel).send(f"```[{current_time}] \n Server : OFF 🟥```")        
            sleep(refresh_time)

    # If you want get multiple server statut, copy and paste line 19 to 29 and create multiple variable for example : "server2 = JavaServer.lookup("play.hypixel.net")" and change the status variable to "status = <your new variable>.status()" 

client.run("<YOUR BOT TOKEN>")

# I'm a beginner so the code is not optimized. But i will upgrade it I think 
# https://github.com/toyaxop/mc_statut_discord_bot
