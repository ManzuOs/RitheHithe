import discord
import asyncio

from PIL import Image
from discord.ext import commands


class avatar(commands.Cog):
  def __init__(self, client):
        self.client = client
  
  
  @commands.command()
  async def avatar(self,ctx, member :discord.Member = None):
    if member is None:
      embed = discord.Embed(title="This command is used like this: ```rhavatar [member]```", colour=0xff0000, timestamp=ctx.message.created_at)
      await ctx.send(embed=embed)
      return
    else:
      embed2 = discord.Embed(title=f"{member}'s Avatar!", colour=0x0000ff, timestamp=ctx.message.created_at)  
  
      embed2.set_image(url = member.avatar_url)
      await ctx.send(embed=embed2)



  @commands.command()
  async def slap(self, ctx, member: discord.Member):
    user = ctx.author
    filename = "images/avatar1.png"
    await user.avatar_url.save(filename)
    
    filename2 = "images/avatar2.png"
    await member.avatar_url.save(filename2)
    
  

    size1 = (100,100)

    size2 = (624,324)

    img = Image.open("images/avatar1.png").convert("RGBA")
    img = img.resize(size1,Image.ANTIALIAS)
    print(img.size)

    img2 = Image.open("images/avatar2.png").convert("RGBA")
    img2 = img2.resize(size1,Image.ANTIALIAS)


    background = Image.open("images/slap-image.jpg")

    print(background.size)

    background = background.resize(size2,Image.ANTIALIAS)

    background.paste(img, (270, 50), img)
    background.paste(img2, (120,120),img2)
    background.save('images/merged_image.jpg',"JPEG")

    with open('images/merged_image.jpg', 'rb') as f:
      picture = discord.File(f)
    await ctx.send(file=picture)




  @commands.command()
  async def knock(self,ctx , member:discord.Member):
    user = ctx.author
    filename = "images/avatar1.png"
    await user.avatar_url.save(filename)
    
    filename2 = "images/avatar2.png"
    await member.avatar_url.save(filename2)
    
  

    size1 = (100,100)

    size2 = (624,324)

    img = Image.open("images/avatar1.png").convert("RGBA")
    img = img.resize((120,120),Image.ANTIALIAS)
    print(img.size)

    img2 = Image.open("images/avatar2.png").convert("RGBA")
    img2 = img2.resize(size1,Image.ANTIALIAS)


    background = Image.open("images/kickbutt-image.png")

    print(background.size)

    background = background.resize(size2,Image.ANTIALIAS)

    background.paste(img, (155, 30), img)
    background.paste(img2, (360,28),img2)
    background.save('images/merged_image.jpg',"JPEG")

    with open('images/merged_image.jpg', 'rb') as f:
      picture = discord.File(f)
    await ctx.send(file=picture)




def setup(client):
    client.add_cog(avatar(client))

    
