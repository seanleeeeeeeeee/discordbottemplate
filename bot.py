from discord.ext.commands import Bot,Context
from discord import Intents
from random import randint
from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyBYIdPNigKKqZobSX09x_w-JC_HRVyibF8"
my_cse_id = "16875384dfc844459"

def google(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']



bot = Bot('>',intents=Intents.all())

def add(num: int, num2 : int):
    return f"{num + num2}"

def subtract(num: int, num2 : int):
    return f"{num - num2}"

def mult(num: int, num2 : int):
    return f"{num * num2}"

def div(num: int, num2 : int):
    return f"{num / num2}"

num = 0


@bot.command()
async def setnumber(ctx: Context):
    global num
    num = randint(1, 100)

@bot.command()
async def guess(ctx: Context, num1: int):
    global num
    if num1 != num:
        await ctx.send("no ur retarded")
    else:
        await ctx.send("omg u got it dubs")


@bot.command()
async def calc(ctx: Context, opt: str, num1: int, num2: int):
    if opt == "add":
        await ctx.send(add(num1, num2))
    elif opt == "sub":
        await ctx.send(subtract(num1, num2))
    elif opt == "mult":
        await ctx.send(mult(num1, num2))
    elif opt == "div":
        await ctx.send(div(num1, num2))

@bot.command()
async def search(ctx: Context, term: str):
    results = google(term, my_api_key, my_cse_id, num=10)
    await ctx.send(results[1]['title'] + ' ' + results[1]['formattedUrl'])

@bot.command()
async def wiki(ctx: Context, term: str):
    results = google(term + ' site:en.wikipedia.org', my_api_key, my_cse_id, num=10)
    await ctx.send(results[1]['title'] + ' ' + results[1]['formattedUrl'])

with open("token") as f:
    t = f.readline()

bot.run(t)