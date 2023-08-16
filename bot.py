import os
from typing import Any 

from disnake.ext import commands

class Bot(commands.InteractionBot):
    def __init__(self, **options: Any):
        super().__init__(**options)