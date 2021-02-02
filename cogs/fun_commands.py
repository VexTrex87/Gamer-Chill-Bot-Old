import discord
from discord import Color as discord_color
from discord.ext import commands

import random

class fun_commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["8ball"])
    async def _8ball(self, context, *, question):
        RESPONSES = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

        embed = discord.Embed(
            title = random.choice(RESPONSES)
        )

        embed.add_field(
            name = "Question",
            value = question
        )

        await context.send(embed = embed)

def setup(client):
    client.add_cog(fun_commands(client))