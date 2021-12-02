import discord
from discord.ui import Select, View , Button
from discord_together import DiscordTogether

#all Select stuff
option1 = discord.SelectOption(label='Youtube', description="Watch youtube with your gang!")
option2 = discord.SelectOption(label='Chess', description="Play chess with your gang!")
option3 = discord.SelectOption(label='Poker', description="Play poker with your gang!")
option4 = discord.SelectOption(label='Betrayal', description="Play betrayal with your gang!")
option5 = discord.SelectOption(label='Fishing', description="Play Fishing with your gang!")
option6 = discord.SelectOption(label='Letter-tile', description="Play Letter-tile with your gang!")
option7 = discord.SelectOption(label='Word-snack', description="Watch Word-snack with your gang!")


Bot = discord.Bot()

@Bot.event
async def on_ready():
    Bot.togetherControl = await DiscordTogether("OTE0ODIzMzE3OTUxNzYyNDgz.YaSpmw.UM9lYoU_gbvWPTLyeW9JreS5bm0")
    print("Bot has logged in  Youtube Watch Together")

@Bot.slash_command(guild_ids=[895920665411076097])
async def watch(
        ctx,
):
    #Making a Visually-Good looking embed
    voice_state = ctx.author.voice

    if voice_state is None:
        await ctx.respond("This command cannot be used unless you are in a VC")
        return

    embed= discord.Embed(title="Which activity do you want to perform?" , description="Choose an activity using the select menu below." , color=discord.Color(0xe6f2ff))

    #lets listen for output,
    async def button_callback(interaction):
        if interaction:
            await ctx.respond("Activity cancelled")
            return

    async def button_callbac2(interaction):
        link = await Bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube', max_uses=1)
        if interaction:
            await ctx.respond(f'Join using [**Click here to join YouTube!**]({link})')
            return

    button = Button(label="Yes",style=discord.ButtonStyle.success)
    button2 = Button(label="No", style=discord.ButtonStyle.danger)
    button2.callback = button_callback
    button.callback =button_callbac2

    async def select_callback(interaction):
            view=View()
            view.add_item(button)
            view.add_item(button2)
            msg=await ctx.respond("do you wish to continue?" , view=view)


    menu = Select(placeholder="You find yourself in a confusing place.",options=[option1])
    menu.callback = select_callback
    view = View()
    view.add_item(menu)

    await ctx.respond(view=view, embed=embed)
    return


Bot.run("OTE0ODIzMzE3OTUxNzYyNDgz.YaSpmw.UM9lYoU_gbvWPTLyeW9JreS5bm0")