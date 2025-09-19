import discord
from discord import app_commands
from datetime import datetime
import pytz

# Define the timezones
timezones = {
    "Denmark": "Europe/Copenhagen",
    "Seattle": "America/Los_Angeles",
    "Salt Lake City": "America/Denver"
}
GUILD_ID = 0

class TimeBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        print(f"Slash commands synced to guild {GUILD_ID}")

client = TimeBot()

@client.tree.command(name="gettime", description="Get the current time in Denmark, Seattle, and Salt Lake City.")
async def gettime(interaction: discord.Interaction):
    response = "**Current Times:**\n"
    for city, tz in timezones.items():
        now = datetime.now(pytz.timezone(tz))
        date_str = now.strftime('%Y-%m-%d')
        military_time = now.strftime('%H:%M:%S')       # 24-hour format
        twelve_hour_time = now.strftime('%I:%M:%S %p') # 12-hour format with AM/PM
        response += f"{city}: {date_str} | {military_time} | {twelve_hour_time}\n"
    await interaction.response.send_message(response)
# Run the bot
client.run("test")
