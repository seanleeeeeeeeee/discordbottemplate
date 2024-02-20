from discord.ext.commands import Bot,Context
from discord import Intents
from random import randint
bot = Bot('>',intents=Intents.all())

# from here you can edit to make more commands


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
async def guess(ctx: Context. num1: int):
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

bot.run("MTIwOTU1MTEyNjc3MzUwMjAwMw.GnHKkm.NCNiOzd87Xx0u6g19KuMKj5lEM-x6jikMYWIbE")