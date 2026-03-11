import os
import discord
from discord.ext import tasks, commands
from datetime import datetime, timedelta

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1479700883444076596

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# CONFIGURACION EVENTOS
blood_start = (4, 0)   # primer Blood del dia
devil_start = (4, 30)  # primer Devil del dia
interval = 120         # cada 2 horas

king_hour = 20

def next_event(start_hour, start_minute):
    now = datetime.now()
    start_today = now.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)

    while start_today < now:
        start_today += timedelta(minutes=interval)

    return start_today

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    check_events.start()

@tasks.loop(minutes=1)
async def check_events():
    channel = bot.get_channel(CHANNEL_ID)
    now = datetime.now()

    blood_next = next_event(*blood_start)
    devil_next = next_event(*devil_start)

    # BLOOD CASTLE
    if (blood_next - now).total_seconds() <= 600 and (blood_next - now).total_seconds() > 540:
        await channel.send("@everyone ⚔️ Blood Castle en 10 minutos!")

    # DEVIL SQUARE
    if (devil_next - now).total_seconds() <= 600 and (devil_next - now).total_seconds() > 540:
        await channel.send("@everyone 👿 Devil Square en 10 minutos!")

    # KING OF MU
    if now.hour == 19 and now.minute == 50:
        await channel.send("@everyone 👑 King of MU comienza en 10 minutos!")

bot.run(TOKEN)
