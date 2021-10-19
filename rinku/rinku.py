from redbot.core import commands
import discord

class Rinku(commands.Cog):
    """Hajime's personal cog."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def usercount(self, ctx):
        """Check my user count!"""
        users=len(self.bot.users)
        await ctx.send(f"I currently have {users} users.")

    @commands.command()
    async def membercount(self, ctx):
        """Shows a guilds member count."""
        mc=len(ctx.guild.members)
        await ctx.send(f"{ctx.guild} currently has {mc} members. With the owner, {ctx.guild.owner}")

    @commands.command()
    async def happyaround(self,ctx):
        """Try it and see."""
        await ctx.send("DONUTS!")

    @commands.command()
    async def cmdcount(self,ctx):
        """How many commands do I have?"""
        counter=humanize_number(len(set(self.bot.walk_commands())))
        await ctx.send(f"I currently have {counter} commands. Have you use all of them? <:HajimePeek:877032884668620822>")