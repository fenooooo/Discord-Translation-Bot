
import os
import discord
from discord.ext import commands
from googletrans import Translator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!")

# Set up the bot
bot = commands.Bot(command_prefix=PREFIX)
translator = Translator()

@bot.event
async def on_ready():
    print(f"Logged in as {{bot.user}}")

@bot.command(name='translate', help="Translates a message to a specified language. Usage: !translate <language_code> <message>")
async def translate(ctx, lang, *, message):
    try:
        translation = translator.translate(message, dest=lang)
        await ctx.send(f'Translated ({lang}): {translation.text}')
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

bot.run(TOKEN)
