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
async def audience(ctx, *, reason: str):
    target_channel = bot.get_channel(1148298812453040158)
    if target_channel:
        audience_message = f"{ctx.author.id} has requested an audience for {reason}"
        await target_channel.send(audience_message)
    else:
        await ctx.send('Invalid target channel ID.')

@bot.command()
async def help(ctx):
    help_message = """
    **Commands:**
    - `!report {channel_id} {user_id} {reason}`: Report a user to a specific channel.
    - `!audience {reason}`: Request an audience for a reason.
    - `!add {user_id}`: Add user to the trusted users list.
    - `!help`: display this.
    """
    await ctx.send(help_message)

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


@bot.command()
async def add(ctx, user_id: int):
    # Check if the user running the command is the owner of the bot
    if ctx.author.id == 637623311773335572:
        trusted_users.append(user_id)
        
        # Save the updated trusted users list to the file
        with open("trustedUsers.txt", "a") as file:
            file.write(f"{user_id}\n")
        
        await ctx.send(f"User {user_id} has been added to the trusted users list.")
    else:
        await ctx.send('You are not authorized to use this command.')


def run(token):
    bot.run(token)
