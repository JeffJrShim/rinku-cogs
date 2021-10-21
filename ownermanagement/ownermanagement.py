from redbot.core import commands

class OwnerManagement(commands.Cog):
    """Owner management utilities."""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(invoke_without_command="True")
    @commands.is_owner()
    async def owner(self,ctx):
        """Owner management commands"""
        if ctx.invoked_subcommand is None:
            bois=next(iter(self.bot.owner_ids))
            await ctx.send(f"Current Bot Owner IDs:\n{bois}")

    @owner.command(invoke_without_command="True")
    @commands.is_owner()
    async def add(self, ctx, *, user: discord.User):
        """Add an owner. Be sure to note that adding the user as an owner will give that user access to everything on your bot. Use this command at your own risk."""
        user=self.bot.get_user(user.id)
        self.bot.owner_ids.add(user.id)
        msg=f"{user} is now a bot owner. Do note that this user currently **has access to everything on the bot, including being able to remove you from ownership** If you've done this by mistake, please do `{ctx.prefix}owner remove {user.id}`"
        await ctx.send(msg)
