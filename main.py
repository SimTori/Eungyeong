import os

import discord as di
from discord.ext import commands

import crawling

bot = commands.Bot(command_prefix="!")


def insertL(data, j, k):
    result = ''
    for i in range(j, k):
        space = ''
        if len(data[0][i]) < 13:
            for q in range(len(data[0][i]), 15):
                space = space + '　'
        elif len(data[0][i]) == 13:
            space = space + '　　'
        else:
            space = space + '　　'

        result = result + str(data[0][i]) + space + str(data[1][i]) + '\n'
    return result


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print('--------------')
    print(bot.guilds)


@bot.command(name='채권')
async def display(ctx, server: str):
    data = crawling.crwaling(server)
    embed = di.Embed(colour=di.Colour.dark_gold())
    embed.set_author(name="채권")
    embed.add_field(name='옷감', value=insertL(data, 1, 5), inline=False)
    embed.add_field(name='가죽', value=insertL(data, 6, 10), inline=False)
    embed.add_field(name='목재', value=insertL(data, 11, 15), inline=False)
    embed.add_field(name='철 주괴', value=insertL(data, 16, 20), inline=False)
    await ctx.send(embed=embed)


@display.error
async def display_error(ctx, error):
    error_msg = "!채권 서버명\n"
    error_msg += "ex) !채권 하제"

    embed = di.Embed(colour=di.Colour.dark_gold())
    embed.set_author(name="채권 명령어")
    embed.add_field(name="명령어", value=error_msg, inline=False)

    embed.add_field(name="서버 목록", value="누이, 하제, 다후타, 모르페우스, 환락", inline=False)
    await ctx.send(embed=embed)


bot.run(os.environ['token'])
