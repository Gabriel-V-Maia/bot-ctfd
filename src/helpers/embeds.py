import discord
import os

from dotenv import load_dotenv


load_dotenv()
channel_id = os.getenv("channel_id")


async def send_embed(bot_client, title:str , content: str, color) -> bool:
    embed = discord.Embed(
        title=title,
        description=content,
        color = color
    )

    channel = await bot_client.fetch_channel(channel_id) 

    if channel:
        await channel.send(embed=embed)
        return True
    else:
        print("channel wasn't found")
        return False


    
