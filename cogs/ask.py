from disnake.ext import commands
from disnake import (
    ApplicationCommandInteraction
)

def setup(bot: "Bot"):
    bot.add_cog(Ask(bot))


class Ask(commands.Cog):
    def __init__(self, bot: "Bot"):
        self.bot = bot

    """
    Driver function for querying OpenAI 
    """
    @commands.slash_command(name="ask", description="Ask the AI anything!")
    async def ask(self, inter: ApplicationCommandInteraction, prompt):

        """
        Send a response when a user types in /ask <args>. 
        """
        await inter.send("Give me a second to think...") 

        
        response = await prompt()

        """
        @TODO: Replace above message from the bot with the result. Add some fancy loading things?
        inter.send(response)
        """

