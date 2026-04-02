import os
import discord

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("token")
DISCORD_CHANNEL = os.getenv("channel_id")

print(f"iniciando na versão {discord.__version__}")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'we have logged in as {client.user}')
    channel = await client.fetch_channel(DISCORD_CHANNEL)

    online_embed = discord.Embed(
        title="Bot está online!",
        description="Bot ficou online, estarei vigiando por novos desafios...",
        color=discord.Color.green()
    )

    if channel:
        await channel.send(embed=online_embed)
    else:
        print("no channel found")
    
client.run(BOT_TOKEN)
