import discord
import asyncio
import random
import time

playing = False
client = discord.Client()

startup = False
door = False
path1 = False
path2 = False
path3 = False
hole = False
holeGold = False
end = False

before_run = False
before_run_2 = False

@client.event
async def on_ready():
    print("ready")
@client.event
async def on_message(message):
    global playing
    global startup
    global door
    global path1
    global path2
    global path3
    global hole
    global holeGold
    global end
    author = str(message.author.id)
    content = str(message.content)
    channel = message.channel
    async def run():
        if startup == True:
            await channel.send("-You are in a dark room. Moonlight shines through the window\n\n"
                               "-There is GOLD in the corner, along with a SHOVEL and a ROPE\n\n"
                               "-There is a DOOR to the EAST\n\n"
                               "-Command?")
            print("At startup")
        elif door == True:
            await channel.send("-Reap your reward\n\n"
                               "-PALE LUNA SMILES AT YOU\n\n"
                               "-You are in a forest. There are paths to the NORTH, WEST, and EAST\n\n"
                               "-Command?")
            print("At door")
        elif path1 == True:
            await channel.send("-Reap your reward\n\n"
                               "-PALE LUNA SMILES AT YOU\n\n"
                               "-You are in a forest. There are paths to the NORTH, WEST, and EAST\n\n"
                               "-Command?")
            print("At path1")
        elif path2 == True:
            await channel.send("-Reap your reward\n\n"
                               "-PALE LUNA SMILES AT YOU\n\n"
                               "-You are in a forest. There are paths to the NORTH, WEST, and EAST\n\n"
                               "-Command?")
            print("At path2")
        elif path3 == True:
            time.sleep(2)
            await channel.send("-PALE LUNA SMILES WIDE")
            time.sleep(2)
            await channel.send("-There are no paths")
            time.sleep(2)
            await channel.send("-PALE LUNA SMILES WIDE")
            time.sleep(2)
            await channel.send("-The ground is soft.")
            time.sleep(2)
            await channel.send("-PALE LUNA SMILES WIDE")
            time.sleep(2)
            await channel.send("-Here.")
            time.sleep(2)
            await channel.send("-Command?")
            print("At path3")
        elif hole == True:
            await channel.send("-There is now a HOLE.")
            print("At hole")
        elif holeGold == True:
            await channel.send("-The GOLD is in the HOLE")
            print("At holeGold")
        elif end == True:
            await channel.send("-Congratulations\n\n"
                               "—— 40.24248 ——\n\n"
                               "——121.4434 ——")
            print("At end")
    if author != "775853758017175633":

        if holeGold == True:
            if content == "FILL_HOLE":
                startup = False
                door = False
                path1 = False
                path2 = False
                path3 = False
                hole = False
                holeGold = False
                end = True

        if hole == True:
            if content == "DROP_GOLD":
                startup = False
                door = False
                path1 = False
                path2 = False
                path3 = False
                hole = False
                holeGold = True
                end = False

        if path3 == True:
            if content == "DIG_HOLE":
                startup = False
                door = False
                path1 = False
                path2 = False
                path3 = False
                hole = True
                holeGold = False
                end = False

        if path2 == True:
            if content == "GO_NORTH":
                await channel.send("ctrl+alt+del")
            if content == "GO_EAST":
                await channel.send("ctrl+alt+del")

            if content == "USE_SHOVEL":
                await channel.send("-Not now.")
            if content == "USE_GOLD":
                await channel.send("-Not here.")
            if content == "USE_ROPE":
                await channel.send("-Used this.")

            if content == "GO_WEST":
                startup = False
                door = False
                path1 = False
                path2 = False
                path3 = True
                hole = False
                holeGold = False
                end = False

        if path1 == True:
            if content == "GO_NORTH":
                await channel.send("ctrl+alt+del")
            if content == "GO_WEST":
                await channel.send("ctrl+alt+del")

            if content == "USE_SHOVEL":
                await channel.send("-Not now.")
            if content == "USE_GOLD":
                await channel.send("-Not here.")
            if content == "USE_ROPE":
                await channel.send("-Used this.")

            if content == "GO_EAST":
                startup = False
                door = False
                path1 = False
                path2 = True
                path3 = False
                hole = False
                holeGold = False
                end = False

        if content == ";play":
            startup = True
            door = False
            path1 = False
            path2 = False
            path3 = False
            hole = False
            holeGold = False
            end = False
            playing = True

        if door == True:
            if content == "GO_EAST":
                await channel.send("ctrl+alt+del")
            if content == "GO_WEST":
                await channel.send("ctrl+alt+del")

            if content == "USE_SHOVEL":
                await channel.send("-Not now.")
            if content == "USE_GOLD":
                await channel.send("-Not here.")
            if content == "USE_ROPE":
                await channel.send("-Used this.")

            if content == "GO_NORTH":
                startup = False
                door = False
                path1 = True
                path2 = False
                path3 = False
                hole = False
                holeGold = False
                end = False
        if playing == True and path1 == False and path2 == False and path3 == False:
            if content == "OPEN_DOOR":
                print("OPENED DOOR")
                startup = False
                door = True
                path1 = False
                path2 = False
                path3 = False
                hole = False
                holeGold = False
                end = False
        await run()

client.run("", bot = False)
