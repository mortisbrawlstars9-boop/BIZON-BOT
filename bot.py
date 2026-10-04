import os
import discord
from discord.ext import commands

# Konfiguracja uprawnień bota
uprawnienia = discord.Intents.default()
uprawnienia.members = True  
uprawnienia.message_content = True

bot = commands.Bot(command_prefix="!", intents=uprawnienia)

@bot.event
async def on_ready():
    print(f"Zalogowano pomyślnie jako: {bot.user.name}")
    print("Bot Bizon MMA działa i czeka na nowych członków!")

@bot.event
async def on_member_join(member):
    # TUTAJ WPISZ ID SWOJEGO KANAŁU POWITALNEGO
    ID_KANALU = 123456789012345678  

    kanal = bot.get_channel(ID_KANALU)
    if kanal is not None:
        tekst = f"WITAMY W RODZINIE BIZON MMA, {member.mention}!"
        nazwa_obrazka = "obrazek.png" 

        if os.path.exists(nazwa_obrazka):
            plik = discord.File(nazwa_obrazka, filename="obrazek.png")
            await kanal.send(content=tekst, file=plik)
        else:
            await kanal.send(content=f"{tekst}\n*(Błąd: Nie znaleziono pliku obrazek.png)*")

# Wklej TUTAJ swój nowy, świeży token wygenerowany z portalu Discorda
TOKEN = "MTU1NjMwNzMxMDY5NDExMzQwMQ.Gcujyg.vQJ99oAFAHP0xXkjv0yHS0ZEJU_Y6ml44t89sU"
bot.run(TOKEN)
