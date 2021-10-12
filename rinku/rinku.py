from redbot.core import commands
import discord

class Rinku(commands.Cog):
    """Hajime's personal cog."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def usercount(self, ctx):
        """This does stuff!"""
        users=len(self.bot.users)
        await ctx.send(f"I currently have {users} users.")

    @commands.command()
    async def membercount(self, ctx):
        """Shows a guilds member count."""
        mc=len(guild.members)
        await ctx.send(f"{ctx.guild} currently has {mc} members. With the owner, {ctx.guild.owner}")

    @commands.command()
    async def happyaround(self,ctx):
        """Try it and see."""
        await ctx.send("DONUTS!")
