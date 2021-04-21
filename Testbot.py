import discord
from discord.ext import commands
import random

from googleapiclient.discovery import build
import discord.channel
import discord.message
from discord.message import Message
import discord.guild
from discord.guild import Guild
import pprint
import asyncio
##import pyRandomdotOrg

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?',description=description)

lastMentioned = ""
@bot.event
async def on_ready():
    guild = bot.guilds[0]
    chann = guild.channels[0]
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(bot)

@bot.event
async def on_message(message):
    if(lastMentioned == null):
        lastMentioned = ""
    if("jimmy" in message.content.lower() ):
        if(message.author.name == lastMentioned):
            await message.channel.send("You really think of me that way, huh " + message.author.name + "?")
        else:    
            await message.channel.send("You're not talking about me, are you " + message.author.name + "?")
            lastMentioned = message.author.name


@bot.command(pass_context=True)
async def define(ctx, *text: str):
    finaltext = 'define '
    for word in text:
        finaltext = finaltext + word  + " "
    
    api_key = "AIzaSyDEI9ei37MeTgaDyQhayyXSdHPM8ZJ4Gfk"
    cse_id = "001464282721790659668:_ja4f_we2rk"
    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']    
    results = google_search(finaltext, api_key, cse_id, num=1)
    for result in results:
        formatText="```" + result['snippet'] + "```"
        await ctx.send(formatText)
@bot.command(pass_context=True)
async def search(ctx,*text : str):
    print('got here')

    """Searches google for an image described by input"""
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
        formatText = "" + result['link'] + ""
        await ctx.send(formatText)
@bot.command()
async def jimmy():
    """In case I'm not here obviously"""
    random.seed()
    #await bot.say(foo)

@bot.command()
async def Noice(pass_context=True):
    await bot.say("http://is2.4chan.org/vg/1486404760144.gif")

@bot.command(pass_context=True)
async def roll(ctx,dice : str):
    """Rolls a dice in NdN format."""
    try:
            rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    if(rolls > 50 or limit > 50):
        result = 'HEY NOW THAT\'S A LOTTA DICE!'
    else:
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))
@bot.command(pass_context=True)
async def KrillMe(ctx):
    """Posts Krill"""
    await ctx.send("https://prod-media.coolaustralia.org/wp-content/uploads/2013/05/06205928/billandwill.jpg")

@bot.command()
async def Stalin():
    """Posts Stalin"""
    await bot.say("http://imgur.com/gallery/jXMUIYP")
@bot.command()
async def Kojimbo():
    """Kojima-san"""
    await bot.say("http://static1.gamespot.com/uploads/original/43/434805/3064712-1248675325-Hideo.jpg")
@bot.command(pass_context=True)
async def repeat(ctx, times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))
@bot.command()
async def Mike(amount : int):
    """The best FORTRAN programmer"""
    await bot.say("https://i1.rgstatic.net/ii/profile.image/AS%3A272457688940593@1441970383991_l/Mike_Roggenkamp.png " * amount)
@bot.command(pass_context=True)
async def hotdogs(ctx, amount : int):
    """Posts a set amount of hotdogs based on input"""
    await ctx.send( ":hotdog: " * amount)
@bot.command()
async def Hariotttt():
    """Post ainsley"""
    await bot.say("https://ih0.redbubble.net/image.37276369.1324/flat,800x800,075,f.u2.jpg")
@bot.command()
async def JoJo():
    """Asks if JOJO"""
    await bot.say("http://i3.kym-cdn.com/photos/images/original/001/195/575/abf.jpg")
@bot.command()
async def Tides():
    """How quickly the tides turn"""
    await bot.say("http://i1.kym-cdn.com/photos/images/original/001/072/409/23c.gif")
@bot.command(pass_context=True)
async def meme(ctx, message):
    await ctx.send( message, tts=1)
    return 'boop'
@bot.command()
async def Delet():
    """Posts Delet this"""
    await bot.say("http://imgur.com/a/QrzQV")

bot.run("MjYxNDkwODE2NzQzMTEyNzA0.Cz1-Yg.mUHdeAMQqEWxYfor9UiXk6UnhPg")