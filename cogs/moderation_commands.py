import discord
from discord import Color as discord_color
from discord.ext import commands

import math

class moderation_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check_any(commands.is_owner(), commands.has_permissions(manage_messages = True))
    async def clear(self, context, amount = 1):
        try:
            deleted_messages = await context.channel.purge(limit = amount + 1)
            deleted_messages_count = len(deleted_messages) - 1
        except Exception as error_message:
            embed = discord.Embed(
                title = f"ERROR: Something went wrong when deleting {str(amount)} messages",
                colour = discord_color.red()
            )
            
            embed.add_field(
                name = "Error Message",
                value = str(error_message)
            )

            await context.send(embed = embed)
        else:
            await context.send(embed = discord.Embed(
                title =  f"SUCCESS: {str(deleted_messages_count)} messages were deleted", 
                colour = discord_color.green()
            ))

    @commands.command()
    @commands.check_any(commands.is_owner(), commands.has_permissions(kick_members = True))
    async def kick(self, context, member: discord.Member, *, reason = None):
        try:
            await member.kick(reason = reason)
        except Exception as error_message:
            embed = discord.Embed(
                title = f"ERROR: Something went wrong when kicking {str(member)}",
                colour = discord_color.red()
            )
            
            embed.add_field(
                name = "Error Message",
                value = str(error_message)
            )

            await context.send(embed = embed)
        else:
            await context.send(embed = discord.Embed(
                title = f"SUCCESS: {str(member)} was kicked", 
                colour = discord_color.green()
            ))

    @commands.command()
    @commands.check_any(commands.is_owner(), commands.has_permissions(ban_members = True))
    async def ban(self, context, member: discord.Member, *, reason = None):
        try:
            await member.ban(reason = reason)
        except Exception as error_message:
            embed = discord.Embed(
                title = f"ERROR: Something went wrong when banning {str(member)}",
                colour = discord_color.red()
            )
            
            embed.add_field(
                name = "Error Message",
                value = str(error_message)
            )

            await context.send(embed = embed)
        else:
            await context.send(embed = discord.Embed(
                title = f"SUCCESS: {str(member)} was banned", 
                colour = discord_color.green()
            ))

    @commands.command()
    @commands.check_any(commands.is_owner(), commands.has_permissions(ban_members = True))
    async def unban(self, context, *, member):
        try:
            banned_users = await context.guild.bans()
            member_name, member_discriminator = member.split("#")

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await context.guild.unban(user)
                    break
        except Exception as error_message:
            embed = discord.Embed(
                title = f"ERROR: Something went wrong when unbanning {str(member)}",
                colour = discord_color.red()
            )
            
            embed.add_field(
                name = "Error Message",
                value = str(error_message)
            )

            await context.send(embed = embed)
        else:
            await context.send(embed = discord.Embed(
                title = f"SUCCESS: {str(member)} was unbanned", 
                colour = discord_color.green()
            ))

def setup(client):
    client.add_cog(moderation_commands(client))