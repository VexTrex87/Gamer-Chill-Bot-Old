import discord
from discord import Color as discord_color
from discord.ext import commands

from datetime import datetime
import time
import json

start_time = datetime.now()
up_time = None

def format_time(sec):
    return time.strftime('%H:%M:%S', time.gmtime(sec))

class default_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, context):
        # default commands
        
        default_commands_embed = discord.Embed(
            title = "Default Commands"
        )
        
        default_commands_embed.add_field(
            name = "help",
            value = "Returns a list of commands. No permissions required. Included in the `default_commands` set.", 
            inline = False
        )

        default_commands_embed.add_field(
            name = "ping",
            value = "Returns the user's ping. No permissions required. Included in the `default_commands` set.", 
            inline = False
        )

        default_commands_embed.add_field(
            name = "info",
            value = "Returns the bot start time, bot up time, and connected servers. No permissions required. Included in the `default_commands` set.", 
            inline = False
        )

        # bot commands

        bot_management_commands_embed = discord.Embed(
            title = "Bot Management Commands" 
        )
        
        bot_management_commands_embed.add_field(
            name = "load <SET>",
            value = "Loads <SET> to update. `Administrator` permissions required. Not included in a set.", 
            inline = False
        )

        bot_management_commands_embed.add_field(
            name = "unload <SET>",
            value = "Loads <SET> to update. `Administrator` permissions required. Not included in a set.",
            inline = False
        )

        bot_management_commands_embed.add_field(
            name = "reload <SET>",
            value = "Unloads and loads <SET> to update. `Administrator` permissions required. Not included in a set.",
            inline = False
        )

        bot_management_commands_embed.add_field(
            name = "checkforupdates",
            value = "Unloads and loads all sets to update. `Administrator` permissions required. Not included in a set.",
            inline = False
        )

        bot_management_commands_embed.add_field(
            name = "changeprefix <NEW_PREFIX = !>",
            value = "Changes the bot's prefix to <NEW_PREFIX>. `Administrator` permissions required. Not included in a set.",
            inline = False
        )

        # fun commands

        fun_commands_embed = discord.Embed(
            title = "Fun Commands"
        )
        
        fun_commands_embed.add_field(
            name = "8ball <QUESTION>",
            value = "Returns a random answer to the <QUESTION>. No permissions required. Included in the `fun_commands` set.", 
        )

        # moderation commands

        moderation_commands_embed = discord.Embed(
            title = "Moderation Commands", 
        )
        
        moderation_commands_embed.add_field(
            name = "clear <AMOUNT = 1>",
            value = "Clears <AMOUNT> messages in the executed channel. Manage `messages permission` required. Included in the `moderation_commands` set.", 
            inline = False
        )

        moderation_commands_embed.add_field(
            name = "kick <USER> <REASON = NONE>",
            value = "Kicks the <USER> from the server with an optional <REASON>. `Kick` permission required. Included in the `moderation_commands` set.", 
            inline = False
        )

        moderation_commands_embed.add_field(
            name = "ban <USER> <REASON = NONE>",
            value = "Bans the <USER> from that server with an optional <REASON>. `Ban` permission required. Included in the `moderation_commands` set.", 
            inline = False
        )

        moderation_commands_embed.add_field(
            name = "unban <USER>",
            value = "Unbans <UESR> from the server. `Ban` permissions required. Included in the `moderation_commands` set.", 
            inline = False
        )

        await context.send(embed = default_commands_embed)
        await context.send(embed = bot_management_commands_embed)
        await context.send(embed = fun_commands_embed)
        await context.send(embed = moderation_commands_embed)

    @commands.command()
    async def ping(self, context):
        ping = round(self.client.latency * 1000)

        embed = discord.Embed(
            title = f"Your ping is {str(ping)} ms",
            colour = (ping < 65 and discord_color.green) or (ping > 170 and discord_color.from_rgb(255, 255, 0)) or (discord_color.red)
        )

        embed.add_field(title = )

        await context.send()
            
    @commands.command()
    async def info(self, context):
        embed = discord.Embed(
            title = "Bot Info",
        )
        
        embed.add_field(
            name = "Start Time", 
            value = start_time, 
            inline = False
        )

        embed.add_field(
            name = "Up Time", 
            value = format_time(start_time - datetime.now()), 
            inline = False
        )

        embed.add_field(
            name = "Connected Servers", 
            value = str(len(self.client.guilds)), 
            inline = False
        )
        
        await context.send(embed = embed)

def setup(client):
    client.add_cog(default_commands(client))