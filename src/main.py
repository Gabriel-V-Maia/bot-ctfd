import os
import discord

from discord.ext import tasks
from dotenv import load_dotenv
from helpers import embeds
from tracker.tracker import Tracker

load_dotenv()

BOT_TOKEN = str(os.getenv("token"))
DISCORD_CHANNEL = os.getenv("channel_id")

def main():
    print(f"Iniciando na versão {discord.__version__} do discord.py")

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    t = Tracker(
        URL_API=os.getenv("URL_API_CHALLENGES"),
        API_KEY=os.getenv("API_KEY"),
        NTFY_TOPIC=os.getenv("NTFY_TOPIC"),
        ARQUIVO_ESTADO="vistos.json",
        DISCORD_CLIENT=client
    )

    @tasks.loop(minutes=6)
    async def checar():
        await t.checar_novos()

    @client.event
    async def on_ready():
        print(f"Logado como {client.user}")
        await embeds.send_embed(client, "Bot online", "O bot está online!", discord.Color.green())
        checar.start()

    client.run(BOT_TOKEN)

if __name__ == "__main__":
    main()
