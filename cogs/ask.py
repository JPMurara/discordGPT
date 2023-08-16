from disnake.ext import commands
from disnake import (
    ApplicationCommandInteraction
)

def setup(bot: "Bot"):
    bot.add_cog(Ask(bot))


class Ask(commands.Cog):
    def __init__(self, bot: "Bot"):
        self.bot = bot

    @commands.slash_command(name="ask", description="Ask the AI anything!")
    async def ask(self, inter: ApplicationCommandInteraction):
        """" Here is where we can parse the GPT results to the user """
        await inter.send(gpt_stuff) 
