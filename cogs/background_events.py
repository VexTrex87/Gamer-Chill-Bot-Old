import discord
from discord.ext import commands

import json

async def get_first_text_channel(client, guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            return channel

class background_events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")   
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        first_text_channel = get_first_text_channel(self.client, self.guild)
        first_text_channel.send(discord.Embed(
            title = f"{str(member)} has joined the server",
        ))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        first_text_channel = get_first_text_channel(self.client, self.guild)
        first_text_channel.send(discord.Embed(
            title = f"{str(member)} has left the server",
        ))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):    
        with open("settings.json", "r") as unloaded_data:
            loaded_data = json.load(unloaded_data)

        if not str(guild.id) in loaded_data["server_data"]:
            loaded_data["server_data"][str(guild.id)] = loaded_data["default_data"].copy()

            with open("settings.json", "w") as unloaded_data2:
                json.dump(loaded_data, unloaded_data2, indent = 4)

            unloaded_data2.close()
        unloaded_data.close()

    @commands.Cog.listener()
    async def on_guild_available(self, guild):
        with open("settings.json", "r") as unloaded_data:
            loaded_data = json.load(unloaded_data)

        if not str(guild.id) in loaded_data["server_data"]:
            loaded_data["server_data"][str(guild.id)] = loaded_data["default_data"].copy()

            with open("settings.json", "w") as unloaded_data2:
                json.dump(loaded_data, unloaded_data2, indent = 4)

            unloaded_data2.close()
        unloaded_data.close()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("settings.json", "r") as unloaded_data:
            loaded_data = json.load(unloaded_data)

        if str(guild.id) in loaded_data["server_data"]:
            del loaded_data["server_data"][str(guild.id)]

            with open("settings.json", "w") as unloaded_data2:
                json.dump(loaded_data, unloaded_data2, indent = 4)

            unloaded_data2.close()
        unloaded_data.close()
    
def setup(client):
    client.add_cog(background_events(client))