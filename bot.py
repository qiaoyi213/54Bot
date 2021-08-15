from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from dislash import InteractionClient, SelectMenu, SelectOption

load_dotenv()

TOKEN = getenv('TOKEN')

bot = commands.Bot(command_prefix='!')
slash = InteractionClient(bot)


@slash.command(
    name="hello", # Defaults to function name
    description="Says hello",
     # If not specified, the command is registered globally
    # Global registration takes up to 1 hour
)
async def hello(inter):
    await inter.reply("Hello!")

@bot.event
async def on_ready():
    print(">>>54BOT is online<<<")


@bot.command()
async def echo(ctx,*, arg):
    await ctx.send(arg)

@slash.command(
    name="hello", # Defaults to function name
    description="Says hello",
    # If not specified, the command is registered globally
    # Global registration takes up to 1 hour
)
async def hello(inter):
    await inter.reply("Hello!")

@bot.command()
async def show_menu(ctx):
    msg = await ctx.send(
        "This message has a select menu!",
        components=[
            SelectMenu(
                custom_id="test",
                placeholder="Choose up to 2 options",
                max_values=2,
                options=[
                    SelectOption("Option 1", "value 1"),
                    SelectOption("Option 2", "value 2"),
                    SelectOption("Option 3", "value 3")
                ]
            )
        ]
    )
    # Wait for someone to click on it
    inter = await msg.wait_for_dropdown()
    # Send what you received
    labels = [option.label for option in inter.select_menu.selected_options]
    await inter.reply(f"Options: {', '.join(labels)}")



bot.run(TOKEN)


