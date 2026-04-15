import discord
from discord.ext import commands

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Command for simple presentation
@bot.command()
async def present(ctx):
    await ctx.send('Hello! I am a Discord bot created to assist you!')

# Command for greeting
@bot.command()
async def greet(ctx):
    await ctx.send('Greetings! How can I help you today?')

# Run the bot with your token
# Make sure to replace 'YOUR_TOKEN_HERE' with your actual bot token
# bot.run('YOUR_TOKEN_HERE')
