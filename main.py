import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils import misc

load_dotenv()

class BauCuaBot(commands.Bot):
    def __init__(self):
        self.description = "Bau Cua Bot"
        super().__init__(
            command_prefix = commands.when_mentioned_or('!'),
            owner_id = 476438504868544525,
            description = self.description,
            case_insensitive = True,
            activity = discord.Activity(name="!help", type=discord.ActivityType.listening),
        )

    async def on_ready(self):
        print(f'connected to discord as {self.user} at {misc.get_formated_ICT_time()}')

bot = BauCuaBot()

@bot.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Load {extension} Cog Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unload {extension} Cog Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Reload {extension} Cog Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def reloadall(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f"cogs.{filename[:-3]}")
            bot.load_extension(f"cogs.{filename[:-3]}")
    await ctx.send(f"Reload All Cogs Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send(f"Shutdown Bot Successfully")
    await bot.close()

@bot.command(hidden=True)
@commands.is_owner()
async def updateactivity(ctx, activity_name):
    await bot.change_presence(activity=discord.Game(name=activity_name))
    await ctx.send(f"Update Activity Successfully")

@bot.command(hidden=True)
@commands.is_owner()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)}ms")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(os.getenv('DISCORD_TOKEN'))