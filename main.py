import asyncio
import cleverbotfree
import discum   
import os

TOKEN = os.environ.get("DISCORD_TOKEN")
bot=discum.Client(token=TOKEN)

@bot.gateway.command
def chatter(resp):
    if resp.event.message:
        message = resp.parsed.auto()
        if message['content'].startswith('c.'):
            username = message['author']['username']
            if username == "Azazel":
                with cleverbotfree.sync_playwright() as p_w:
                    c_b = cleverbotfree.Cleverbot(p_w)
                    user_input = message['content'].split("c.")[1]
                    answer = c_b.single_exchange(user_input)
                    bot.sendMessage(message['channel_id'], answer)

from subprocess import Popen, PIPE
import sys

p = Popen([sys.executable, "-m", "playwright", "install"], stdin=PIPE, stdout=PIPE, stderr=PIPE)


bot.gateway.run(auto_reconnect=True)