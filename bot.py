import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise ValueError(
        'Token do Discord não encontrado. '
        'Certifique-se de que o arquivo .env existe e contém DISCORD_TOKEN=seu_token_aqui'
    )

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado com sucesso como {bot.user}!')

@bot.command(name='apresenta')
async def apresenta(ctx):
    embed = discord.Embed(
        title='👋 Olá! Eu sou o Cadu!',
        description=(
            'Sou um bot criado para ajudar neste servidor Discord.\n\n'
            '**Criado por:** Eduardo\n'
            '**Prefixo de comandos:** `!`\n'
            '**Use** `!ajuda` **para ver todos os meus comandos.**'
        ),
        color=discord.Color.blue()
    )
    embed.set_footer(text='Cadu Bot • Sempre pronto para ajudar!')
    await ctx.send(embed=embed)

@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'🏓 Pong! Latência: **{latency}ms**')

@bot.command(name='ajuda')
async def ajuda(ctx):
    embed = discord.Embed(
        title='📋 Comandos Disponíveis',
        description='Aqui estão todos os comandos que você pode usar:',
        color=discord.Color.green()
    )
    embed.add_field(name='`!apresenta`', value='O bot se apresenta com informações pessoais.', inline=False)
    embed.add_field(name='`!ping`',      value='Mostra a latência atual do bot.',             inline=False)
    embed.add_field(name='`!ajuda`',     value='Lista todos os comandos disponíveis.',        inline=False)
    embed.set_footer(text='Use ! antes de cada comando.')
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            '❌ Comando não encontrado. Use `!ajuda` para ver os comandos disponíveis.'
        )
    else:
        await ctx.send('⚠️ Ocorreu um erro ao executar o comando. Tente novamente.')

bot.run(TOKEN)
