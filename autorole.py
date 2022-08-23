import discord 
from discord.ext import commands

intents = discord.Intents().all()
Client = commands.Bot(command_prefix="-", intents=intents)


@Client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='ROLENAME')    
    await member.add_roles(role)



Client.run('TOKEN')