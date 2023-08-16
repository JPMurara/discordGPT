import openai
from disnake.ext import commands
from disnake import (
    ApplicationCommandInteraction
)


def setup(bot: "Bot"):
    bot.add_cog(Ask(bot))


class Ask(commands.Cog):
    def __init__(self, bot: "Bot"):
        self.bot = bot

    def ask_openai(self, prompt):
        messages = [
            {"role": "system", "content": "you are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            message=messages,
        )

        return response['choices'][0]['message']['content'].strip()

    @commands.slash_command(name="ask", description="Ask the AI anything!")
    async def ask(self, inter: ApplicationCommandInteraction, prompt):
        """
        Send a response when a user types in /ask <args>. 
        """
        await inter.response.defer()

        await inter.followup.send("Give me a second to think...")

        response = self.ask_openai(prompt)

        await inter.followup.send(content=response)

        """
        @TODO: Replace above message from the bot with the result. Add some fancy loading things?
        inter.send(response)
        """
