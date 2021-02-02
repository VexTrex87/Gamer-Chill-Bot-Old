import discord
from discord import Color as discord_color
from discord.ext import commands

import os
import json

def get_prefix(client, context):
    with open("settings.json", "r") as unloaded_data:
        loaded_data = json.load(unloaded_data)

    prefix = loaded_data["server_data"][str(context.guild.id)]["prefix"]
    unloaded_data.close() 

    return prefix

with open("settings.json", "r") as unloaded_data:
    loaded_data = json.load(unloaded_data)

default_prefix = loaded_data["default_data"]["prefix"]
token = loaded_data["bot_data"]["token"]
unloaded_data.close() 

client = commands.Bot(command_prefix = get_prefix)

@client.command()
@commands.check_any(commands.is_owner(), commands.has_permissions(administrator = True))
async def load(context, extention):
    try:
        client.load_extension(f"cogs.{extention}")
    except Exception as error_message:
        embed = discord.Embed(
            title =  f"ERROR: {extention} was unable to load",
            colour = discord_color.red()
        )
        
        embed.add_field(
            name = "Error Message",
            value = str(error_message)
        )

        await context.send(embed = embed)
    else:
        await context.send(embed = discord.Embed(
            title =  f"SUCCESS: {extention} was loaded", 
            colour = discord_color.green()
        ))

@client.command()
@commands.check_any(commands.is_owner(), commands.has_permissions(administrator = True))
async def unload(context, extention):
    try:
        client.unload_extension(f"cogs.{extention}")
    except Exception as error_message:
        embed = discord.Embed(
            title =  f"ERROR: {extention} was unable to unload", 
            colour = discord_color.red()
        )
        
        embed.add_field(
            name = "Error Message",
            value = str(error_message)
        )

        await context.send(embed = embed)
    else:
        await context.send(embed = discord.Embed(
            title =  f"SUCCESS: {extention} was unloaded", 
            colour = discord_color.green()
        ))

@client.command()
@commands.check_any(commands.is_owner(), commands.has_permissions(administrator = True))
async def reload(context, extention):
    try:
        client.reload_extension(f"cogs.{extention}")
    except Exception as error_message:
        embed = discord.Embed(
            title =  f"ERROR: {extention} was unable to reload", 
            colour = discord_color.red()
        )
        
        embed.add_field(
            name = "Error Message",
            value = str(error_message)
        )

        await context.send(embed = embed)
    else:
        await context.send(embed = discord.Embed(
            title =  f"SUCCESS: {extention} was reloaded", 
            colour = discord_color.green()
        ))

@client.command()
@commands.check_any(commands.is_owner(), commands.has_permissions(administrator = True))
async def update(context):
    try:
        for file_name in os.listdir("./cogs"):
            if file_name.endswith(".py"):
                client.reload_extension(f"cogs.{file_name[:-3]}")
    except Exception as error_message:
        embed = discord.Embed(
            title =  f"ERROR: Could not check for updates", 
            colour = discord_color.red()
        )
        
        embed.add_field(
            name = "Error Message",
            value = str(error_message)
        )

        await context.send(embed = embed)
    else:
        await context.send(embed = discord.Embed(
            title =  "SUCCESS: Bot up to date", 
            colour = discord_color.green()
        ))

@commands.command()
@commands.check_any(commands.is_owner(), commands.has_permissions(administrator = True))
async def changeprefix(self, context, prefix = default_prefix):
    try:
        if not isinstance(prefix, str):
            context.send("ERROR: Prefix (`{prefix}`) is not a string")

        with open("settings.json", "r") as unloaded_data:
            loaded_data = json.load(unloaded_data)

        if not str(guild.id) in loaded_data["server_data"]:
            loaded_data["server_data"][str(context.guild.id)]["prefix"] = prefix

            with open("settings.json", "w") as unloaded_data2:
                json.dump(loaded_data, unloaded_data2, indent = 4)

            unloaded_data2.close()
        unloaded_data.close()

    except Exception as error_message:
        embed = discord.Embed(
            title =  f"ERROR: Could not change prefix to `{prefix}`",
            colour = discord_color.red()
        )
        
        embed.add_field(
            name = "Error Message",
            value = str(error_message)
        )

        await context.send(embed = embed)
    else:
        await context.send(embed = discord.Embed(
            title = f"SUCCESS: Prefix changed to `{prefix}`",
            colour = discord_color.green()
        ))

def main():
    client.remove_command("help")

    for file_name in os.listdir("./cogs"):
            if file_name.endswith(".py"):
                client.load_extension(f"cogs.{file_name[:-3]}")

    client.run(token)

if __name__ == "__main__":
    main()