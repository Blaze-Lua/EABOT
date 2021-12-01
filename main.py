import discord
from discord.ui import Select, View

#all Select stuff
option1 = discord.SelectOption(label='Youtube', description="Watch youtube with your gang!"),
option2 = discord.SelectOption(label='Chess', description="Play chess with your gang!"),
option3 = discord.SelectOption(label='Poker', description="Play poker with your gang!")
option4 = discord.SelectOption(label='Betrayal', description="Play betrayal with your gang!")
option5 = discord.SelectOption(label='Fishing', description="Play Fishing with your gang!")
option6 = discord.SelectOption(label='Letter-tile', description="Play Letter-tile with your gang!")
option7 = discord.SelectOption(label='Word-snack', description="Watch Word-snack with your gang!")
option8 = discord.SelectOption(label='Doodle-crew', description="Play Doodle-crew with your gang!")
option9 = discord.SelectOption(label='Spellcast', description="Play spellcast with your gang!")
option10 = discord.SelectOption(label='Checkers-in-the-park', description="Play checkers with your gang!")
option11 = discord.SelectOption(label='Awkword', description="Play awkword with your gang!")

Bot = discord.Bot()

@Bot.event
async def on_ready():
    print("Bot has logged in  Youtube Watch Together")

@Bot.slash_command(guild_ids=[895920665411076097])
async def watch(
        ctx,
):
    #Making the select Menu
    menu = Select(placeholder="You find yourself in a confusing place.",min_values=15,options=[option1 ,option2,option3,option4,option5,option6,option7,option8,option9,option10,option11])

    view = View()
    view.add_item(menu)

    #Making a Visually-Good looking embed
    embed= discord.Embed(title="Which activity do you want to perform?" , description="Choose an activity using the select menu below." , color=discord.Color(0xe6f2ff))


    #sending both of them
    await ctx.respond(view=view , embed=embed)

Bot.run("OTE0ODIzMzE3OTUxNzYyNDgz.YaSpmw.UM9lYoU_gbvWPTLyeW9JreS5bm0")