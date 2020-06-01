import asyncio
import atexit
import json
import logging
import os

from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import discord

CLIENT = discord.Client()
logging.basicConfig()

# Dumb way to save state
servers_path = Path("servers.cfg")
servers = defaultdict(list)
if servers_path.exists():
    with servers_path.open("r") as f:
        servers.update(json.loads(f))


atexit.register(lambda: json.dump(servers, servers_path.open("w")))


@CLIENT.event
@asyncio.coroutine
def on_ready():
    logging.info("PigeonBot is online")


SEND_MESSAGE_EXECUTOR = ThreadPoolExecutor(20)


async def send_message(client, dst_ch, content):
    return CLIENT.send_message(CLIENT.get_channel(dst_ch), content)


@CLIENT.event
async def on_message(message):
    if message.content.startswith("^p subscribe"):
        try:
            src_ch_id, dst_ch_id = message.content.split()[2:4]
        except:
            await send_message(CLIENT, message.channel.id, "LOL that didn't work")
        else:
            listening = servers[src_ch_id]
            if dst_ch_id not in listening:
                listening.append(dst_ch_id)
    elif message.content.startswith("^p unsubscribe"):
        try:
            src_ch_id, dst_ch_id = message.content.split()[2:4]
        except:
            await send_message(CLIENT, message.channel.id, "LOL that didn't work")
        else:
            listening = servers[src_ch_id]
            if dst_ch_id in listening:
                listening.remove(dst_ch_id)
    else:
        listening = servers.get(message.channel.id, [])
        await asyncio.gather(
            *(send_message(CLIENT, dst_ch, message.content) for dst_ch in listening)
        )


@CLIENT.event
@asyncio.coroutine
def on_server_join(server):
    logging.info(server)


if __name__ == "__main__":
    CLIENT.run(os.getenv("email"), os.getenv("password"))
