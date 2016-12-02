import os

import discord
import asyncio

CLIENT = discord.Client()
PREVIOUS_MESSAGES = [ None ]
@CLIENT.event
@asyncio.coroutine
def on_ready():
    print("PigeonBot is online")

@CLIENT.event
@asyncio.coroutine
def on_message(message):
    if message.server.name.startswith("IHANA") and \
               message.channel.name == "live_calls" and \
               message.author.name == "IHA BDO Bot":
       print("Relaying message.")

       if PREVIOUS_MESSAGES[0] is not None:
           try:
               yield from CLIENT.delete_message(PREVIOUS_MESSAGES[0])
           finally:
               PREVIOUS_MESSAGES[0] = None


       message = yield from CLIENT.send_message(CLIENT.get_channel("254051680222445568"), message.content)
       PREVIOUS_MESSAGES[0] = message

@CLIENT.event
@asyncio.coroutine
def on_server_join(server):
    print(server)

if __name__ == "__main__":
    CLIENT.run(os.getenv("email"), os.getenv("password"))
