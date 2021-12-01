import discord
from discord.ui import Select,View


class Options:

    def __init__(self):
        print('Loading options')


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
