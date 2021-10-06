from .rinku import Rinku


def setup(bot):
    bot.add_cog(Rinku(bot))
