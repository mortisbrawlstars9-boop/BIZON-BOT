import os
import discord
from discord.ext import commands

# Konfiguracja uprawnień bota
uprawnienia = discord.Intents.default()
uprawnienia.members = True  # Wymagane do wykrywania nowych osób
uprawnienia.message_content = True

bot = commands.Bot(command_prefix="!", intents=uprawnienia)

@bot.event
async def on_ready():
    print(f"Zalogowano pomyślnie jako: {bot.user.name}")
    print("Bot Bizon MMA działa i czeka na nowych członków!")

@bot.event
async def on_member_join(member):
    # TUTAJ WPISZ ID SWOJEGO KANAŁU POWITALNEGO (musisz włączyć tryb deweloperski na Discordzie, kliknąć prawym przyciskiem myszy na kanał i wybrać "Kopiuj ID")
    ID_KANALU = 123456789012345678  
    
    kanal = bot.get_channel(ID_KANALU)
    if kanal is not None:
        tekst = f"WITAMY W RODZINIE BIZON MMA, {member.mention}!"
        
        # Nazwa Twojego obrazka umieszczonego w tym samym folderze
        nazwa_obrazka = "obrazek.png" 
        
        if os.path.exists(nazwa_obrazka):
            plik = discord.File(nazwa_obrazka, filename="obrazek.png")
            await kanal.send(content=tekst, file=plik)
        else:
            await kanal.send(content=f"{tekst}\n*(Błąd: Nie znaleziono pliku graficznego o nazwie obrazek.png)*")

# Wklej swój token bota w cudzysłowie poniżej
TOKEN = "MTU1NjMwNzMxMDY5NDExMzQwMQ.G8UyLI.SKxtUpcEP1wp_z9dvCITUwOSdsqVd-njfe4BIE"
bot.run(TOKEN)