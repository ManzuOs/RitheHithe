import discord
import os

from dotenv import load_dotenv
from keep_alive import keep_alive
from discord.ext import commands
from dislash import InteractionClient

client = commands.Bot(command_prefix='rh',
                      intents=discord.Intents.all(),
                      help_command=None,
                      status=discord.Status.do_not_disturb,
                      activity=discord.Activity(
                          type=discord.ActivityType.watching,
                          name="𝑹𝒊𝒕𝒉𝒆𝑯𝒊𝒕𝒉𝒆™"))

slash = InteractionClient(client)

load_dotenv()
TOKEN = os.environ['.env']


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded {extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
client.run(TOKEN)
