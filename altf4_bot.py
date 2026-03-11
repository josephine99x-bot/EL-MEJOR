import os
import discord
from discord.ext import tasks, commands
from datetime import datetime, timedelta

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1479700883444076596

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# CONFIGURACION EVENTOS
blood_interval = 120
devil_interval = 120

blood_next = datetime.now() + timedelta(minutes=47)
devil_next = datetime.now() + timedelta(minutes=77)

king_hour = 20

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    check_events.start()

@tasks.loop(minutes=1)
async def check_events():
    global blood_next, devil_next

    channel = bot.get_channel(CHANNEL_ID)
    now = datetime.now()

    # BLOOD CASTLE
    if 0 <= (blood_next - now).total_seconds() <= 600:
        await channel.send("@everyone ⚔️ Blood Castle en 10 minutos!")
        blood_next += timedelta(minutes=blood_interval)

    # DEVIL SQUARE
    if 0 <= (devil_next - now).total_seconds() <= 600:
        await channel.send("@everyone 👿 Devil Square en 10 minutos!")
        devil_next += timedelta(minutes=devil_interval)

    # KING OF MU
    if now.hour == king_hour and now.minute == 50:
        await channel.send("@everyone 👑 King of MU comienza en 10 minutos!")

bot.run(TOKEN)
