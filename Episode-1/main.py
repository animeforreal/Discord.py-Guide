import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", case_insensitive=True)

@client.event
async def on_ready():
  print(f"Login as {client.user.name}")
  #NOW SET THE ACTIVITY
  await client.change_presence(activity=discord.Game(name=f"{client.command_prefix}ping"))

@client.command(name="ping")
async def _ping(ctx):
  embed = discord.Embed(title=f"{client.user.name} - PING LATENCY", description=f"Pong: {client.latency}", color=0xff2050)
  await ctx.send(embed=embed)

client.run("TOKEN")
