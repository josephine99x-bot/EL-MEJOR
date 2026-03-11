import os
import discord

from discord.ext import tasks, commands
from datetime import datetime

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1479700883444076596

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    bloodcastle.start()
    dorados.start()
    kingofmu.start()
    superlevel.start()
    devilsquare.start()

@tasks.loop(minutes=1)
async def bloodcastle():
    now = datetime.now()

    if now.minute == 0 and now.hour in [4,6,8,10,12,14,16,18,20,22,0,2]:
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send("⚔️ Blood Castle abierto!")

@tasks.loop(minutes=1)
async def devilsquare():
    now = datetime.now()

    horarios = [
        (4,30),
        (6,30),
        (8,30),
        (10,30),
        (12,30),
        (14,30),
        (16,30),
        (18,30),
        (20,30),
        (22,30),
        (0,30),
        (2,30)
    ]

    if (now.hour, now.minute) in horarios:
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send("👿 **Devil Square abierto!**")

@tasks.loop(hours=9, minutes=53)
async def dorados():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("🐉 Evento Dorados activo!")

@tasks.loop(hours=17, minutes=53)
async def kingofmu():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("👑 King of MU comienza!")

@tasks.loop(minutes=1)
async def superlevel():
    now = datetime.now()
    if now.weekday() in [5,6] and now.hour == 0 and now.minute == 0:
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send("⭐ Evento Super Level activo!")


bot.run(TOKEN)
