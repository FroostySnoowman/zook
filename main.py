import discord
import random
import os
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='~')
client.remove_command('help')

@client.event
async def on_ready():
	activity = discord.Game(name="Use ~help", type=3)
	await client.change_presence(status=discord.Status.dnd, activity=activity)
	print('Bot is up and running :)'.format(client))

@client.event
async def on_member_join(member):
  welcomechannel =  client.get_channel(771904873344008255)
  embed=discord.Embed(title="Welcome", url="", 
  description="Hey {}, welcome! Did you bring your blanket? Come relax and have fun! \n \nHead on down to <#803811521389133824> to see the rest of the server!".format(member.mention), 
  color=discord.Color.green())
  await welcomechannel.send(embed=embed)    
  await member.send(f"Welcome to **{member.guild.name}** head on down to <#803811521389133824> to see the rest of the channels.")

@client.event
async def on_message(message):
  verifychannel = client.get_channel(803811521389133824)
  if message.content != '.verify' and (message.channel == verifychannel) and (message.author.id != 503641822141349888) and (message.author.id != 800578878371397653):
    await message.delete()
    embed=discord.Embed(title="Verification Error", url="", 
    description="Hey! You cannot send that message here. Please type `.verify` in <#803811521389133824> to gain access to the rest of the server.", 
    color=discord.Color.red())
    await message.author.send(embed=embed)
  if message.content == '.verify' and (message.channel == verifychannel):
    verified = discord.utils.get(message.guild.roles, name='Member')
    await message.delete()
    embed=discord.Embed(title="Verification Passed", url="", 
    description="You are now successfully verified, thanks!", 
    color=discord.Color.green())
    await message.author.send(embed=embed)
    await message.author.add_roles(verified)
  await client.process_commands(message)

@client.command()
async def verification1(ctx):
  embed = discord.Embed(title="Verification",
  url ="",
  description="Please type, `.verify` to be verified and gain access to the rest of the server. Thanks :D",
  color=discord.Color.blue())
  await ctx.message.delete()
  await ctx.send(embed=embed)

@client.command()
async def verification2(ctx):
  embed = discord.Embed(title="Verification Problems",
  url ="",
  description="Please PM <@503641822141349888> If You Have Any Issues Verifying.",
  color=discord.Color.blue())
  await ctx.message.delete()
  await ctx.send(embed=embed)

#The code below will set the slowmode on a channel.
@client.command()
@commands.has_permissions(administrator=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!", delete_after=5)
    await ctx.message.delete()

#The code below will clean messages.
@client.command()
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
	await ctx.channel.purge(limit=limit+1)
	await ctx.send('Cleared By: {}'.format(ctx.author.mention), delete_after=2)
	await ctx.message.delete()


@clean.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send("You cannot do that!")

@client.command()
async def anime(ctx):
  await ctx.send('Boop')

@client.command()
@commands.has_permissions(administrator=True)
async def promote(ctx, member: discord.Member, prom = None):
  tmod = discord.utils.get(ctx.guild.roles, name='New-Mod')
  mod = discord.utils.get(ctx.guild.roles, name='Moderator')
  staffupdates = client.get_channel(784977313104003092)

  if prom == 'tmod' :
    await member.add_roles(tmod) 
    await staffupdates.send(f"{member.mention} has been promoted to **New-Mod**! **GG**!")

  elif prom == 'mod' :
    await member.add_roles(mod) 
    await staffupdates.send(f"{member.mention} has been promoted to **Moderator**! **GG!**")

  await ctx.message.delete()

@client.command()
async def staff(ctx):
    embed=discord.Embed(title="Zook Staff Members", url="", 
    description="**__Owner__** » <@282665864065581057> \n \n**__Admin__** » <@503641822141349888> \n**__Admin__** » <@192355974600851456> \n**__Admin__** » <@255303992538693632> \n \n**__Moderator__** » <@286514301085417473> \n**__Moderator__** » <@368770627081076739> \n \n**__New-Mods__** » <@322769397707964416> \n**__New-Mods__** » <@262596371679281152>", 
    color=discord.Color.green())
    embed.set_footer(text = "Bot Developer » Someone#0171")
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()

client.run('')
