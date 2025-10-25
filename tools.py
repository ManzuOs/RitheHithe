import discord
import asyncio
from discord.ext import commands

king = 814747708547792906
admin_role = 814075083131584512


class serverTools(commands.Cog):
    def __init__(self, client):
        self.client = client

##################################################


    @commands.command()
    @commands.has_any_role(king, admin_role)
    async def announce(self, ctx):
        guild = self.client.get_guild(712540205521043488)
        announce_channel = guild.get_channel(815995930821656602)
        announcer = ctx.author

        await ctx.send('Please state your announcement ')

        message = await self.client.wait_for('message')
        await ctx.send(message.author)
        await ctx.send(f'Announcing .......')

        mbed = discord.Embed(color=discord.Color.magenta(),
                             title='From 𝑹𝒊𝒕𝒉𝒆𝑯𝒊𝒕𝒉𝒆™ Administration',
                             description=(message.content))
        if announcer == message.author:

            await announce_channel.send('@everyon')
            await announce_channel.send(embed=mbed)
            await ctx.send("Announced")
        else:
            await ctx.send('New message has appeared,bug still not fixed')
##################DM###################   
    @commands.command()
    async def dm(self,ctx, member : discord.Member):

      await ctx.send(f'What message you want to sent to {member} ')
      def check(m):
        return m.author.id -- ctx.author.id

      message = await self.client.wait_for('message', check=check)
      info = await ctx.send(f'sending messsage to {member}')
      await asyncio.sleep(0.8)
      await info.edit(content='Sended :thumbsup: ')
 
      mbed = discord.Embed(
        color = discord.Color.blue(),
        title = 'From 𝑹𝒊𝒕𝒉𝒆𝑯𝒊𝒕𝒉𝒆™ Administration',
        description = (message.content)
  )

      await member.send(embed=mbed)



##################POLL###################


    @commands.command()
    async def poll(self, ctx, question, option1=None, option2=None):

      if option1 == None and option2 == None:

        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title=f"NEW POLL: {question}", description=f'✅ = Yes\n❎ = No', colour=0xff0000, timestamp=ctx.message.created_at)

        message = await ctx.send(embed=embed)
        await message.add_reaction('✅')
        await message.add_reaction('❎')


      elif option1 == None:

        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
                title=f"NEW POLL: {question}", description=f'✅ = {option1}\n❎ = No', colour=0xff0000, timestamp=ctx.message.created_at)
        message = await ctx.send(embed=embed)
        await message.add_reaction('✅')
        await message.add_reaction('❎')

      elif option2 == None:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
                title=f"NEW POLL: {question}", description=f'✅ = Yes\n❎ = {option2}', colour=0xff0000, timestamp=ctx.message.created_at)
        message = await ctx.send(embed=embed)
        await message.add_reaction('✅')
        await message.add_reaction('❎')

      else:

        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
                title=f"NEW POLL: {question}", description=f'✅ = {option1}\n❎ = {option2}', colour=0xff0000, timestamp=ctx.message.created_at)
        message = await ctx.send(embed=embed)
        await message.add_reaction('✅')
        await message.add_reaction('❎')

###########################

    @commands.command()
    @commands.has_any_role(king, admin_role)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(serverTools(client))
