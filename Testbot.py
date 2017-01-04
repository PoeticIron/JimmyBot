import discord
from discord.ext import commands
import random
from googleapiclient.discovery import build

import pprint

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command()
async def search(*text : str):
    finaltext = " "

    for word in text:
        finaltext = finaltext + word + " "
    
    api_key = "AIzaSyDEI9ei37MeTgaDyQhayyXSdHPM8ZJ4Gfk"
    cse_id = "001464282721790659668:_ja4f_we2rk"

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']

    results = google_search(finaltext, api_key, cse_id, num=1, searchType= 'image')
    for result in results:
        await bot.say(result['link'])

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
            rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return
    if(rolls > 50 or limit > 50):
        result = 'HEY NOW THAT\'S A LOTTA DICE!'
    else:
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))
@bot.command()
async def KrillMe():
    await bot.say("http://coolaustralia.org/wp-content/uploads/2013/05/billandwill.jpg")
@bot.command()
async def Mods():
    await bot.say("Don't mind me, just taking my hotdogs for a walk ( ͡° ͜ʖ ͡°)╯╲___ :hotdog:")
@bot.command()
async def Stalin():
    await bot.say("http://imgur.com/gallery/jXMUIYP")
@bot.command(description='Actually implemented by me')
async def Farage():
    """Does largely Nothing"""
    await bot.say("You can't barrage the farage! http://www.thereveillenwu.com/wp-content/uploads/2016/06/6a00d8341bf8f353ef017eeacb1b2e970d.jpg");
@bot.command()
async def Kojimbo():
    await bot.say("http://static1.gamespot.com/uploads/original/43/434805/3064712-1248675325-Hideo.jpg")
@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))



bot.run("MjYxNDkwODE2NzQzMTEyNzA0.Cz1-Yg.mUHdeAMQqEWxYfor9UiXk6UnhPg")
