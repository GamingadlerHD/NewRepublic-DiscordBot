import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)


# Load trusted users from a file
def load_trusted_users():
    try:
        with open("trustedUsers.txt", "r") as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        return []

trusted_users = load_trusted_users()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def report(ctx, user_id: int, *, reason: str):
    if ctx.author.id in trusted_users:
        channel = bot.get_channel(1148298812453040158)
        if channel:
            report_message = f'<@&1148288347505176647> Please Blacklist {user_id}, Reason: {reason}'
            await channel.send(report_message)
            await ctx.send('Thanks for reporting')
        else:
            await ctx.send('Invalid channel ID.')
    else:
        await ctx.send('You are not authorized to use this command.')


bot.run('token')