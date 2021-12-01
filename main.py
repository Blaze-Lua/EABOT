import discord
from discord.ui import Select,Button,View
from options import Options

Bot = discord.Bot()

@Bot.event
async def on_ready():
    print("Bot has logged in  Youtube Watch Together")

@Bot.slash_command(guild_ids=[895920665411076097])
async def watch(
        ctx,
):
    #Making the select Menu
    menu = Select(placeholder="You find yourself in a confusing place." , options=[Options.option1 , Options.option2,Options.option3,Options.option4,Options.option4,Options.option5,Options.option6,Options.option7,Options.option8,Options.option9,Options.option10,Options.option11])

    view = View()
    view.add_item(menu)

    #Making a Visually-Good looking embed
    embed= discord.Embed(title="Which activity do you want to perform?" , description="Choose an activity using the select menu below." , color=discord.Color(0xe6f2ff))


    #sending both of them
    await ctx.respond(view=view , embed=embed)

Bot.run("OTE0ODIzMzE3OTUxNzYyNDgz.YaSpmw.UM9lYoU_gbvWPTLyeW9JreS5bm0")