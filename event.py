import discord
import datetime
from discord.ext import commands

class ourEvent(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{self.client.user} is connected')

  @commands.Cog.listener()
  async def on_member_join(self,member):
    mbed = discord.Embed(
        color = discord.Color.red(),
        title = 'Welcome Message',
        description = f'Welcome {member.mention}, enjoy your stay!'
    )
    await member.send(embed=mbed)

  @commands.Cog.listener()
  async def on_command_error(self,ctx, error):
    await ctx.send(error) 
    if isinstance(error,commands.errors.CommandInvokeError):
      await ctx.send('loading error')
    if isinstance(error,          commands.errors.MissingRequiredArgument):
      await ctx.send('MANA SOALAN GILAK')
    if isinstance(error,commands.errors.MissingAnyRole):
      await ctx.send('Hey you cannot use that')
  

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.guild)
  async def ping(self, ctx):
    embed = discord.Embed(title=f"🏓Pong! {round(self.client.latency * 1000)}ms",color = discord.Color.blue(), timestamp=datetime.datetime.utcnow())
    await ctx.reply(embed = embed)



  @commands.command()
  async def server_inv(self, ctx):
    link = await ctx.channel.create_invite(max_age = 300)
    mbed = discord.Embed(
        color = discord.Color.blue(),
        title = f'Invitation link for {ctx.author}',
        description = f"{link}"
    )
    await ctx.send(embed=mbed)


def setup(client):
  client.add_cog(ourEvent(client))
      