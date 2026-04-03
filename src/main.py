import os
import discord

from dotenv import load_dotenv
from helpers import embeds

load_dotenv()
BOT_TOKEN = str(os.getenv("token"))
DISCORD_CHANNEL = os.getenv("channel_id")

print(f"iniciando na versão {discord.__version__} do discordpy")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'we have logged in as {client.user}')

    sent_embed = await embeds.send_embed(client, "Bot online", "O bot está online!", discord.colour.Color.green())

    
    
    

client.run(BOT_TOKEN)
