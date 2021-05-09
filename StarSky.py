# -*- coding: utf-8 -*-

##### インポート #####
import discord

from discord.ext import commands
from discord.ext import tasks
from datetime import time
from collections import Counter
from contextlib import redirect_stdout
from discord.ext.commands import Bot

import random
import asyncio
import aiohttp
import os
import subprocess
import sys
import datetime
import time
import ast
import re
import zlib
import io
import requests
import xml.etree.ElementTree as ET
import locale
import traceback
import json
import textwrap
import platform
import uptime

import star_sky_module as s

##### 最初の定義 #####
prefix = commands.when_mentioned_or("s!")

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
##### 変数 #####
no = '👎'
ok = '👍'
left = '⏪'
right = '⏩'
yl = "⬅"
yr = "➡"
counts = 0
col = random.randint(0, 0xFFFFFF)
bcol = 0x03a9fc
dicenum = random.randint(0, 6)
ver = "X"
release = "0.0.0"
updateinfos = "・Heroku稼働"
act = f"s!help | discord.py {discord.__version__} | Python {platform.python_version()} | Build X"
##### リスト #####
admin = [663155028793491477]
subowner = [548058577848238080,345342072045174795]

##### 設定 #####
bot.remove_command('help')
##### 最初の処理 #####
@bot.event
async def on_ready():
    print("ログインに成功しました")
    await bot.change_presence(activity = discord.Game(name="起動しています… | Starry Sky Project"),status = discord.Status.idle)
    print(bot.user.name)
    print(bot.user.id)
    print("起動時の情報を送信しています… / Owner")
    with open("config.json", encoding="utf-8") as f:
        bot.json_config = json.load(f)
    print("[Starry Sky System] config.jsonを読み込みました。")
    bot.load_extension("jishaku")
    print("[Starry Sky System] jishakuを読み込みました。")
    bot.owner_ids = [584008752005513216]
    print("[Starry Sky System] BOTオーナーのIDを、584008752005513216にしました。")
    print("起動時の情報を送信しています… / User")
    print("最終処理を実行しています…")
    await bot.change_presence(activity = discord.Game(name=f"s!help | discord.py {discord.__version__} | Python {platform.python_version()} | Build X"),status=discord.Status.idle)
    print("[Starry Sky System] アクティビティを設定しました。")
    print("Debug Console.")
    for allguild in bot.guilds:
        print(allguild)
    print("[StarSky System] All Done. 全ての初回起動動作は正常に終了しました。")
##### 新evalを使用するのに必要な関数 #####
def cleanup_code(content):
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])
    return content.strip('` \n')
##### デバッグ系コード #####        
@bot.command(name="eval",description="Pythonのソースを評価するよ。\n`BOT運営全員`が使用できるね。")
async def eval_(ctx, *, code: str):
    if ctx.author.id in admin or ctx.author.id in subowner or ctx.author.id == 584008752005513216:

        env = {
            "client": bot,
            "discord": discord,
            "commands": commands,
            "ctx": ctx,
            "import": __import__,
            "bot": bot,
            "_message": ctx.message,
            "_guild": ctx.guild,
            "_author": ctx.author,
            "_channel": ctx.channel,
            "_msg": ctx.message,
            "_mes": ctx.message,
            "_send": ctx.send,
        }

        env.update(globals())

        code = cleanup_code(code)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(code, "  ")}'

        if "os" in code:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`os`は含めることが出来ません。",color=0xff0000))
            return
        elif "token" in code:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`token`は含めることが出来ません。",color=0xff0000))
            return
        elif "TOKEN" in code:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`TOKEN`は含めることが出来ません。",color=0xff0000))
            return
        elif "globals" in code:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`globals`は含めることが出来ません。",color=0xff0000))
            return
        elif "exec" in code:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`exec`は含めることが出来ません。",color=0xff0000))
            return
        elif "import config" in code:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`config`は`import`することが出来ません。",color=0xff0000))
            return
        elif "from config" in code:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`config`は`from`することが出来ません。",color=0xff0000))
            return

        try:
            exec(to_compile, env)
        except Exception as e:
            await ctx.message.add_reaction("❌")

            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.message.add_reaction("❌")

            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:

              await ctx.message.add_reaction("✅")
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                _last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')
    else:
        await s.no_admin(ctx,"admin",0xff0000)
        
@bot.command(name="valu",description="Pythonのソースを評価するよ。\n通常のevalより制限を少なくしたよ。\n`BOTサブオーナー`が使用できるね")
async def eval__(ctx, *, code: str):
    if ctx.author.id in subowner or ctx.author.id == 58400875200553216:


        env = {
            "client": bot,
            "discord": discord,
            "commands": commands,
            "ctx": ctx,
            "import": __import__,
            "bot": bot,
            "_message": ctx.message,
            "_guild": ctx.guild,
            "_author": ctx.author,
            "_channel": ctx.channel,
            "_msg": ctx.message,
            "_mes": ctx.message,
            "_send": ctx.send,
        }

        env.update(globals())

        code = cleanup_code(code)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(code, "  ")}'
        
        if "os" in code:
            await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`os`は含めることが出来ません。",color=0xff0000))
            return
        elif "token" in code:
            await ctx.message.clear_reaction(discord.utils.get(bot.emojis, name="Loading"))
            await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`token`は含めることが出来ません。",color=0xff0000))
            return
        elif "TOKEN" in code:
            await ctx.message.clear_reaction(discord.utils.get(bot.emojis, name="Loading"))
            await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`TOKEN`は含めることが出来ません。",color=0xff0000))
            return
        elif "exec" in code:
            await ctx.message.clear_reaction(discord.utils.get(bot.emojis, name="Loading"))
            await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`exec`は含めることが出来ません。",color=0xff0000))
            return
        elif "import config" in code:
            await ctx.message.clear_reaction(discord.utils.get(bot.emojis, name="Loading"))
            await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`config`は`import`することが出来ません。",color=0xff0000))
            return
        elif "from config" in code:
            await ctx.message.clear_reaction(discord.utils.get(bot.emojis, name="Loading"))
            await ctx.message.add_reaction("‼")
            await ctx.send(embed=discord.Embed(description="`config`は`from`することが出来ません。",color=0xff0000))
            return

        try:

            exec(to_compile, env)

        except Exception as e:
            await ctx.message.add_reaction("❌")
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.message.add_reaction("❌")

            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:await ctx.message.add_reaction("✅")
                
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                _last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')
    else:
        await s.no_admin(ctx,"subowner",0xff0000)
        
@bot.command(aliases=["evalf"],description="制限なしevalだよ。\n`BOTオーナー`しか使用できないよ。")
async def evalfree(ctx, *, code: str):
    if ctx.author.id == 584008752005513216:

        env = {
            "client": bot,
            "discord": discord,
            "commands": commands,
            "ctx": ctx,
            "import": __import__,
            "bot": bot,
            "_message": ctx.message,
            "_guild": ctx.guild,
            "_author": ctx.author,
            "_channel": ctx.channel,
            "_msg": ctx.message,
            "_mes": ctx.message,
            "_send": ctx.send,
        }

        env.update(globals())

        code = cleanup_code(code)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(code, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            await ctx.message.add_reaction("❌")
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.message.add_reaction("❌")
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction("✅")
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                _last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')
    else:
        await s.no_admin(ctx,"owner",0xff0000)
        
@bot.command(description="コマンドの`有効`と`無効`を切り替えるよ。")
@commands.is_owner()
async def command(ctx,mode,command_name):
    cmd = bot.get_command(command_name)
    if mode == "off":
    
        if cmd:
            msg = await ctx.send("**コマンド無効化中・・・**")
            cmd.enabled = False
            await msg.edit(content=f"⭕** | `{cmd}`を`無効`にしたよ。**") 
        elif command_name == "command" or "eval" or "jishaku" or "reboot" or "down" or "shell":
            msg = await ctx.send("**コマンド無効化中・・・**")
            await msg.edit(content=f"❌** | そのコマンドは無効にできないよ。**")
        else:
            msg = await ctx.send("**コマンド無効化中・・・**")
            await msg.edit(content=f"❌** | `{command_name}`っていう名前のコマンドが存在しないよ。**")

    elif mode == "on":
        cmd = bot.get_command(command_name)
    
        if cmd:
            msg = await ctx.send("**コマンド有効化中・・・**")
            cmd.enabled = True
            await msg.edit(content=f"⭕** | `{cmd}`を`有効`にしたよ。**")
        else:
            msg = await ctx.send("**コマンド有効化中・・・**")
            await msg.edit(content=f"❌** | `{command_name}`っていう名前のコマンドが存在しないか、無効化されていないよ。**")
            
    else:
        await ctx.send("❌** | 存在しないモードだよ。**")
        
@bot.command(description="指定したコマンドを削除するよ。\n製作者しか使えないね。\n注意:再起動するまで削除状態になるよ。")
@commands.is_owner()
async def remove(ctx,command_name):
    cmd = bot.get_command(command_name)
    
    if cmd:
        msg = await ctx.send("**コマンド削除中・・・**")
        bot.remove_command(cmd)
        await msg.edit(content=f"⭕** | `{cmd}`を削除したよ。**")
    else:
        msg = await ctx.send("**コマンド削除中・・・**")
        await msg.edit(content=f"❌** | `{command_name}`っていう名前のコマンドが存在しないよ。**")
        
@bot.command(aliases=["sh","system","sys"],description="コマンドプロンプトのコマンドを実行するよ。\n製作者しか使えないね。")
@commands.is_owner()
async def shell(ctx, *, command):
    try:
        e=discord.Embed(title="コマンド実行 - 確認", description="実行する場合は`ok`、しない場合は`x`を送信してください。",color=0x03a9fc,timestamp=datetime.datetime.utcnow())
        e.add_field(name="入力コマンド",value=f"```fix\n{command}\n```",inline=False)
        msg = await ctx.send(embed=e)
        def c(b):
            return b.author.id == ctx.author.id
        try:
            guess = await bot.wait_for("message", timeout=30, check=c)
        except asyncio.TimeoutError:
            e=discord.Embed(description="制限時間が過ぎたため、自動で操作を拒否したよ。")
            await msg.edit(embed=e)
            return
        if guess.content == "ok":
            print("操作開始")
            e=discord.Embed(title="コマンド実行", description="実行中・・・",color=0x03a9fc,timestamp=datetime.datetime.utcnow())
            e.add_field(name="入力コマンド",value=f"```fix\n{command}\n```",inline=False)
            await msg.edit(embed=e)
            result = subprocess.check_call(command.split())
            await ctx.message.add_reaction("✅")
            e=discord.Embed(title="コマンド実行", description="完了",color=0x03a9fc,timestamp=datetime.datetime.utcnow())
            e.add_field(name="入力コマンド",value=f"```fix\n{command}\n```",inline=False)
            e.add_field(name="終了コード",value=f"```c\n{result}\n```",inline=False)
            e.add_field(name="結果",value=f"```diff\n+ 操作は正常に終了しました。\n```",inline=False)
            await msg.edit(embed=e)
            print("操作終了")
            return
        elif guess.content == "x":
            e=discord.Embed(description="操作を拒否したよ。",color=ctx.author.color)
            await msg.edit(embed=e)
            return

        else:
            embed2 = discord.Embed(description="`ok`か`x`で実行してね。", color=0xff0000)
            await msg.edit(embed=embed2)
            return
    except Exception as e:
        await ctx.message.add_reaction("❌")
        e=discord.Embed(title="コマンド実行", description="失敗",color=0x03a9fc,timestamp=datetime.datetime.utcnow())
        e.add_field(name="入力コマンド",value=f"```fix\n{command}\n```",inline=False)
        e.add_field(name="エラー内容",value=f"```py\n{traceback.format_exc(3)}\n```",inline=False)
        e.add_field(name="結果",value="```diff\n- エラーが発生したため、操作はできませんでした。\n```",inline=False)
        await msg.edit(embed=e)
        return
    
@bot.command(aliases=["leaveg","lg"],description="指定したサーバーから退出するよ。\n`gid`にサーバーIDを入れてね。")
@commands.is_owner()
async def leaveguild(ctx, gid):
    try:
        return await bot.get_guild(gid).leave()
        e = discord.Embed(title="サーバー退出", description=f"{gid}から退出したよ。",color=ctx.author.color)
        await ctx.send(embed=e)
    except:
        await ctx.send(embed=discord.Embed(tile="サーバー退出",description="エラーが発生したから、サーバーから退出できなかったよ。",color=0xff0000))
        
@bot.command(aliases=["end","shutdown","close"],description="BOTをシャットダウンするよ。\n製作者しか使えないね。")
@commands.is_owner()
async def down(ctx):
    await ctx.send(embed=discord.Embed(title="シャットダウン", description="BOTをシャットダウンするよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow()))
    await bot.change_presence(activity = discord.Game(name="Shutdown now..."),status=discord.Status.dnd)
    await asyncio.sleep(5)
    await bot.close()
    
@bot.command(aliases=["restart","run","reload"],description="BOTを再起動するよ。\n制作者しか使えないね。")
@commands.is_owner()
async def reboot(ctx):
    e = discord.Embed(title="再起動", description="BOTを再起動するよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=e)
    await bot.change_presence(activity = discord.Game(name="Restart now..."),status=discord.Status.idle)
    await asyncio.sleep(5)
    cmd = "python StarSky.py"
    subprocess.Popen(cmd.split())
    await bot.close()
    
@bot.command(aliases=["activity"],description="BOTのアクティビティを変更するよ。\n`BOTサブオーナー`しか使えないね。")
async def setactivity(ctx, *, status):
    if ctx.author.id in admin or ctx.author.id in subowner or ctx.author.id == 584008752005513216 or 751653229112328283:

        await bot.change_presence(activity = discord.Game(name=f"{status}"),status = discord.Status.idle)
        e = discord.Embed(title="操作成功", description=f"アクティビティを変更したよ。\n現在のアクテビティ:{status}", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_admin(ctx,"subowner",0xff0000)
        
@bot.command(aliases=["resetact","ract"],description="アクティビティをリセットするよ。\n`BOTサブオーナー`しか使えないね。")
async def resetactivity(ctx):
    if ctx.author.id in admin or ctx.author.id in subowner or ctx.author.id == 584008752005513216 or 751653229112328283:
        await bot.change_presence(activity = discord.Game(f"{act}"),status =discord.Status.idle)        
        e = discord.Embed(title="操作成功", description="アクティビティをデフォルトに戻したよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e) 
    else:
        await s.no_admin(ctx,"subowner",0xff0000)
        
@bot.command(aliases=["online"],description="BOTのステータスをオンラインにするよ。\n`BOTサブオーナーとBOT運営`しか使えないね。")
async def setonline(ctx):
    if ctx.author.id in admin or ctx.author.id in subowner or ctx.author.id == 584008752005513216 or 751653229112328283:
        await bot.change_presence(activity = discord.Game(f"{act}"),status =discord.Status.online)        
        e = discord.Embed(title="操作成功", description="ステータスをオンラインにしたよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e) 
    else:
        await s.no_admin(ctx,"subowner",0xff0000)
        
@bot.command(aliases=["idle"],description="BOTのステータスを退席中にするよ。\n`BOTサブオーナーとBOT運営`しか使えないね。")
async def setidle(ctx):
    if ctx.author.id in admin or ctx.author.id in subowner or ctx.author.id == 584008752005513216 or 751653229112328283:
        await bot.change_presence(activity = discord.Game(f"{act}"),status =discord.Status.idle)        
        e = discord.Embed(title="操作成功", description="ステータスを退席中にしたよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e) 
    else:
        await s.no_admin(ctx,"subowner",0xff0000)
        
@bot.command(aliases=["dnd"],description="BOTのステータスを取り込み中にするよ。\n`BOTサブオーナーとBOT運営`しか使えないね。")
async def setdnd(ctx):
    if ctx.author.id in admin or ctx.author.id in subowner or ctx.author.id == 584008752005513216 or 751653229112328283:
        await bot.change_presence(activity = discord.Game(f"{act}"),status =discord.Status.dnd)     
        e = discord.Embed(title="操作成功", description="ステータスを取り込み中にしたよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e) 
    else:
        await s.no_admin(ctx,"subowner",0xff0000)
        
##### BAN&KICK #####
@bot.command(description="指定したユーザーをBANするよ。\nユーザーをKICK出来る人のみ。")
async def kick(ctx, user: discord.User=None,reason=None):
    no = '👎'
    ok = '👍'
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.kick_members) or ctx.guild.owner == ctx.author:
        if user is None:
            e = discord.Embed(title="実行エラー",description="名前を指定してね。",color=0xff0000)
            await ctx.send(embed=e)
        else:
            embeds = discord.Embed(
                title=f"**「@{user.name}」KICKしちゃう？**",color=0xC41415)
            msg = await ctx.send(embed=embeds)
            await msg.add_reaction(no)
            await msg.add_reaction(ok)
            try:
                def predicate1(message,author):
                    def check(reaction,users):
                        if reaction.message.id != message.id or users == ctx.bot.user or author != users:
                            return False
                        if reaction.emoji == ok or reaction.emoji == no:
                            return True
                        return False
                    return check
                react = await ctx.bot.wait_for('reaction_add',timeout=20,check=predicate1(msg,ctx.message.author))
                if react[0].emoji == ok:
                    await ctx.guild.kick(user, reason=reason)
                    print(f"{user.name}が{ctx.message.author.name}によってKICKされたよ。。")
                    embed = discord.Embed(title=f"{user.name}はKICKされたよ。。",color=0xC41415,timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="-------------------------", value=f"名前: **{user.name}**\nID: **{user.id}**\n理由:**{reason}**", inline=False)

                    return await ctx.send(embed=embed)
                elif react[0].emoji == no:
                    embeds = discord.Embed(
                        title=f"{user.name}はKICKされなかったよ。。",color=0x10cfee)
                    return await ctx.send(embed=embeds)
            except asyncio.TimeoutError:
                embeds = discord.Embed(
                    title=f"{user.name}はKICKされなかったよ。。",color=0x10cfee)
                return await ctx.send(embed=embeds)
    else:
        await s.no_per(ctx,"kick",0xff0000)
        
@bot.command(description="指定したユーザーをBANするよ。\nユーザーをBAN出来る人のみ。")
async def ban(ctx, user: discord.User=None,reason=None):
    no = '👎'
    ok = '👍'
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.ban_members) or ctx.guild.owner == ctx.author:
        if user is None:
            e = discord.Embed(title="実行エラー",description="名前を指定してね。",color=0xff0000)
            await ctx.send(embed=e)
        else:
            embeds = discord.Embed(
                title=f"**「@{user.name}」BANしちゃう？**",color=0xC41415)
            msg = await ctx.send(embed=embeds)
            await msg.add_reaction(no)
            await msg.add_reaction(ok)
            try:
                def predicate1(message,author):
                    def check(reaction,users):
                        if reaction.message.id != message.id or users == ctx.bot.user or author != users:
                            return False
                        if reaction.emoji == ok or reaction.emoji == no:
                            return True
                        return False
                    return check
                react = await ctx.bot.wait_for('reaction_add',timeout=20,check=predicate1(msg,ctx.message.author))
                if react[0].emoji == ok:
                    await ctx.guild.ban(user, reason=reason)
                    print(f"{user.name}が{ctx.message.author.name}によってBANされたよ。。")
                    embed = discord.Embed(title=f"{user.name}はBANされたよ。。",color=0xC41415,timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="-------------------------", value=f"名前: **{user.name}**\nID: **{user.id}**\n理由:**{reason}**", inline=False)

                    return await ctx.send(embed=embed)
                elif react[0].emoji == no:
                    embeds = discord.Embed(
                        title=f"{user.name}はBANされなかったよ。。",color=0x10cfee)
                    return await ctx.send(embed=embeds)
            except asyncio.TimeoutError:
                embeds = discord.Embed(
                    title=f"{user.name}はBANされなかったよ。。",color=0x10cfee)
                return await ctx.send(embed=embeds)
    else:
        await s.no_per(ctx,"ban",0xff0000)
##### 役職系コード #####

@bot.command(aliases=["radd"],description="指定したユーザーに役職を付与するよ。\n役職を管理できる人のみ。")
async def roleadd(ctx, member: discord.Member, role: discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        await member.add_roles(role)
        e = discord.Embed(title="操作成功", description=f'{member.mention}さんに{role.mention}を付与したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,role,0xff0000)
        
@bot.command(aliases=["rre"],description="指定したユーザーから役職を削除するよ。\n役職を管理できる人のみ。")
async def roleremove(ctx, member: discord.Member, role: discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        await member.remove_roles(role)
        e = discord.Embed(title="操作成功", description=f'{member.mention}さんから{role.mention}を剥奪したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"role",0xff0000)
        
@bot.command(aliases=["rdel"],description="役職を削除するよ。\n役職を管理できる人のみ。")
async def roledelete(ctx, role: discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        await role.delete()
        e = discord.Embed(title="操作成功", description=f'{role.name}を削除したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,role,0xff0000)
        
@bot.command(aliases=["rcr"],description="役職を作成するよ。\n役職を管理できる人のみ。")
async def rolecreate(ctx, rolename):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        role = await ctx.guild.create_role(name=rolename)
        e = discord.Embed(title="操作成功", description=f'{role.mention}を作成したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"role",0xff0000)
        
@bot.command(aliases=["rusers","ru"],description="役職を持つメンバー一覧を表示するよ。")
async def roleusers(ctx,*,role:discord.Role):           
    try:
        users = "\n".join(list(c.name for c in role.members))
        e = discord.Embed(title=f"{role}を持つメンバー一覧",description=f"```\n{users}\n```",color=ctx.author.color)
        await ctx.send(embed=e)
    except discord.HTTPException:
        await ctx.send("❌** | 表示数が2000文字を超えているため、表示できないよ。。**")
        
@bot.command(aliases=["rcol","rc"],description="役職の色を変更するよ。\n役職を管理できる人のみ。")
async def rolecolor(ctx,role:discord.Role,r:int,g:int,b:int):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        await role.edit(color=discord.Colour.from_rgb(r,g,b))
        e = discord.Embed(title="操作成功", description=f'{role.mention}の色を変更したよ。。\n現在の色(R G B):{r} {g} {b}',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"role",0xff0000)
        
@bot.command(aliases=["roleallmemadd","rama"],description="指定した役職を全メンバーに付与するよ。\n役職を管理できる人のみ。\n※BOT含む")
async def roleallmembersadd(ctx, role:discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        msg = await ctx.send(embed=discord.Embed(title="操作開始", description=f"全員に{role}を付与するよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow()))
        [await member.add_roles(role) for member in ctx.guild.members]
        await msg.edit(embed=discord.Embed(title="操作成功",description=f"{role}を全員に付与したよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow()))
    else:
        await s.no_per(ctx,"role",0xff0000)
        
@bot.command(aliases=["roleallmemremove","roleallmemr","ramr"],description="指定した役職を全メンバーから削除するよ。\n役職を管理できる人のみ。\n※BOT含む")
async def roleallmembersremove(ctx, role:discord.Role):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_roles) or ctx.guild.owner == ctx.author:
        msg = await ctx.send(embed=discord.Embed(title="操作開始", description=f"全員から{role}を剥奪するよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow()))
        [await member.remove_roles(role) for member in ctx.guild.members]
        await msg.edit(embed=discord.Embed(title="操作成功",description=f"{role}を全員から剥奪したよ。", color=ctx.author.color,timestamp=datetime.datetime.utcnow()))
    else:
        await s.no_per(ctx,"role",0xff0000)
##### チャンネル&カテゴリー系コード #####

@bot.command(aliases=["textchannelcr","textchcr","tchc"],description="指定した名前のテキストチャンネルを作成するよ。\nチャンネルを管理できる人のみ。")
async def textchannelcreate(ctx,channel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        channel = await ctx.channel.category.create_text_channel(name=channel)
        e = discord.Embed(title="操作成功", description=f'テキストチャンネル:{channel.mention}を作成したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"channel",0xff0000)
        
@bot.command(aliases=["textchanneldel","textchdel","tchd"],description="指定した名前のチャンネルを削除するよ。\nチャンネルを管理できる人のみ。")
async def textchanneldelete(ctx,channel:discord.TextChannel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        await channel.delete()
        e = discord.Embed(title="操作成功", description=f'テキストチャンネル:{channel.name}を削除したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"channel",0xff0000)
        
@bot.command(aliases=["voicechannelcr","voicechcr","vchc"],description="指定した名前のボイスチャンネルを作成するよ。\nチャンネルを管理できる人のみ。")
async def voicechannelcreate(ctx,channel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        channel = await ctx.channel.category.create_voice_channel(name=channel)
        e = discord.Embed(title="操作成功", description=f'ボイスチャンネル:{channel.name}を作成したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"channel",0xff0000)
        
@bot.command(aliases=["voicechanneldel","voicechdel","vchd"],description="指定した名前のボイスチャンネルを作成するよ。\nチャンネルを管理できる人のみ。")
async def voicechanneldelete(ctx,channel:discord.VoiceChannel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        await channel.delete()
        e = discord.Embed(title="操作成功", description=f'ボイスチャンネル:{channel.name}を削除したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"channel",0xff0000)
        
@bot.command(aliases=["categorycr","ctc"],description="指定した名前のカテゴリーを作成するよ。\nチャンネルを管理できる人のみ。")
async def categorycreate(ctx,category):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        category = await ctx.guild.create_category(name=category)
        e = discord.Embed(title="操作成功", description=f'カテゴリー:{category}を作成したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"channel",0xff0000)
        
@bot.command(aliases=["categorydel","ctd"],description="指定した名前のカテゴリーを削除するよ。\nチャンネルを管理できる人のみ。")
async def categorydelete(ctx,category:discord.CategoryChannel):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        await category.delete()
        e = discord.Embed(title="操作成功", description=f'カテゴリー:{category}を削除したよ。',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"channel",0xff0000)
        
@bot.command(aliases=["chedit","che"],description="コマンドを実行したチャンネル名を変更するよ。\nチャンネルを管理できる人のみ。")
async def channeledit(ctx,channelname):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_channels) or ctx.guild.owner == ctx.author:
        await ctx.channel.edit(name=f"{channelname}")
        e = discord.Embed(title="操作成功", description=f'チャンネル名を変更したよ。\n現在のチャンネル名:{channelname}',color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"channel",0xff0000)
##### メッセージ系コード #####

@bot.command(aliases=["cl","clean","purge","pu"],description="指定した件数のメッセージを削除するよ。\nメッセージを管理できる人のみ。")
async def clear(ctx, num:int):
    if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_messages) or ctx.guild.owner == ctx.author:
        try:
            await ctx.channel.purge(limit=num)
            e = discord.Embed(title="メッセージ削除", description=f"{num}件のメッセージを削除したよ。",color=ctx.author.color,timestamp=datetime.datetime.utcnow())
            l = await ctx.send(embed=e)
            await asyncio.sleep(3)
            await l.delete()
        except IndexError:
            e = discord.Embed(title="メッセージ削除", description="引数が不正だね・・・",color=0xff0000)
            await ctx.send(embed=e)
    else:
        await s.no_per(ctx,"message",0xff0000)
        
@bot.command(aliases=["acl","allclean","allpurge","apu"],description="チャンネル内のメッセージを全て削除するよ。\nメッセージを管理できる人のみ。\n※誤爆注意")
async def allclear(ctx):
    try:
        if (ctx.guild.me.top_role < ctx.author.top_role and ctx.author.guild_permissions.manage_messages) or ctx.guild.owner == ctx.author:
            check_menu = "このチャンネルのメッセージを全て削除するよ・・・\n実行する場合は`ok`、やめる場合は`no`と送信してね・・・\n**__一度実行してしまったら、BOTを止める、サーバーから退出させる、権限をなくす以外対処法はないよ。__**\n**__もし間違って実行してしまった場合には、如何なる理由があろうとも製作者は責任を負いません。__**"
            embed = discord.Embed(title="確認画面", description=check_menu, color=0xff0000)
            embed.set_footer(text="責任を持って実行して！(10秒で自動拒否されるよ)",)
            mes = await ctx.send(embed=embed)
            def c(b):
                return b.author.id == ctx.author.id
            try:
                guess = await bot.wait_for("message", timeout=10, check=c)
            except asyncio.TimeoutError:
                e=discord.Embed(description="制限時間が過ぎたため、自動で操作を拒否したよ。")
                await mes.edit(embed=e)
                return
            if guess.content == "ok":
                e = discord.Embed(title="全メッセージ削除",descriptionn="チャンネルの全メッセージ削除を開始するよ。")
                await ctx.channel.purge()
                e = discord.Embed(title="全メッセージ削除", description=f"チャンネルのメッセージを全て削除したよ。",color=ctx.author.color,timestamp=datetime.datetime.utcnow())
                l = await ctx.send(embed=e)
                await asyncio.sleep(3)
                await l.delete()
            elif guess.content == "no":
                return
                e=discord.Embed(description="操作を拒否したよ。",color=ctx.author.color)
                await mes.edit(embed=e)
            else:
                return 
                embed2 = discord.Embed(description="`ok`か`no`で実行してね。", color=0xff0000)
                await ctx.send(embed=embed2)
        else:
            await s.no_per(ctx,"message",0xff0000)
    except:
        e=discord.Embed(title="操作失敗", description=f"エラーが発生したよ。\n```py\n{traceback.format_exc()}```",color=0xff0000)
        await ctx.send(embed=e)
        
@bot.command(aliases=["messagehis","mhis"],description="指定した数のメッセージの履歴を表示するよ。")
async def messagehistory(ctx, num:int):
    async for i in ctx.channel.history(limit=num):
        await ctx.send(f"{i.author.name}#{i.author.discriminator}: {i.content}")
##### 情報系コード #####

@bot.command(name="info",aliases=["about"],description="BOTの情報を表示するよ。\n※`userinfo`とは異なるよ。")
async def info_(ctx):
    fist = discord.Embed(title="BOT情報", description=f"**__{bot.user.name}__**\n製作者:{bot.get_user(584008752005513216)}\nDiscord Bot For Operation\ndiscord.py v{discord.__version__} | rewrite\nPython {platform.python_version()}",color=0x03a9fc)
    fist.set_thumbnail(url=ctx.bot.user.avatar_url)
    fist.add_field(name="ページの操作方法",value="➡:次のページに進むよ。\n⬅:前にページに戻るよ。\n🗑:このメッセージを削除するよ。\n⏹:このメッセージを表示したまま処理を停止するよ。",inline=False)
    e1 = discord.Embed(title="BOT情報 - Info", color=0x03a9fc)
    e1.set_thumbnail(url=ctx.bot.user.avatar_url)
    e1.add_field(name="ボットオーナー",value=bot.get_user(584008752005513216).name, inline=False)
    e1.add_field(name="ボットサブオーナー",value="\n".join(bot.get_user(s).name for s in subowner), inline=False)
    e1.add_field(name="ボット運営",value="\n".join(bot.get_user(s).name for s in admin), inline=False)
    e1.add_field(name="導入サーバー数", value=f"{len(bot.guilds)}", inline=False)
    e1.add_field(name="利用ユーザー数", value=f"{len(bot.users)}", inline=False)
    e2 = discord.Embed(title="BOT情報 - System", color=0x03a9fc)
    e2.set_thumbnail(url=ctx.bot.user.avatar_url)
    e2.add_field(name="言語", value=f"Python {platform.python_version()}", inline=False)
    e2.add_field(name="discord.py バージョン",value=discord.__version__)
    e2.add_field(name="バージョン情報", value=f"```css\nVer:{ver}\nRelese:{release}```", inline=False)
    e2.add_field(name="現在合計コマンド数", value=f"{len(bot.commands)}", inline=False)
    e2.add_field(name="OS",value=f"`{platform.platform()}`", inline=False)
    e2.add_field(name="アップデート情報",value=f"```fix\n{updateinfos}\n```", inline=False)
    e3 = discord.Embed(title="BOT情報 - URL", color=0x03a9fc)
    e3.set_thumbnail(url=ctx.bot.user.avatar_url)
    e3.add_field(name="招待リンク", value=f"[{bot.user.name}](https://discord.com/api/oauth2/authorize?client_id=797378859199627284&permissions=4228906231&scope=bot)",inline=False)
    e3.add_field(name="参考サイト", value="[APIリファレンス](https://discordpy.readthedocs.io/en/latest/api.html)｜[Python-izm 基礎編](https://www.python-izm.com/basic/)", inline=False)
    page_count = 0 #ヘルプの現在表示しているページ数
    page_content_list = [fist, e1, e2, e3] #ヘルプの各ページ内容
    send_message = await ctx.send(embed=page_content_list[0]) #最初のページ投稿
    await send_message.add_reaction("➡")
    await send_message.add_reaction("🗑")
    await send_message.add_reaction("⏹")
    
    def help_react_check(reaction,user):
        emoji = str(reaction.emoji)
        if reaction.message.id != send_message.id:
            return 0
        if emoji == "➡" or emoji == "⬅" or emoji == "🗑" or emoji == "⏹":
            if user != ctx.author:
                return 0
            else:
                return 1
    while not bot.is_closed():
        try:
            reaction,user = await bot.wait_for('reaction_add',check=help_react_check,timeout=30.0)
        except asyncio.TimeoutError:
            await send_message.clear_reactions()
            await send_message.add_reaction("❌")
            return #時間制限が来たら、それ以降は処理しない
        else:
            emoji = str(reaction.emoji)
            if emoji == "➡":
                page_count += 1
            if emoji == "⬅":
                page_count -= 1
            if emoji == "⏹":
                await send_message.clear_reactions()
                await send_message.add_reaction("❌")
                return
            if emoji == "🗑":
                await send_message.delete()
                return
            await send_message.clear_reactions() #事前に消去する
            await send_message.edit(embed=page_content_list[page_count])

            if page_count == 0:
                await send_message.add_reaction("➡")
                await send_message.add_reaction("🗑")
                await send_message.add_reaction("⏹")

            if page_count == 1:
                await send_message.add_reaction("⬅")
                await send_message.add_reaction("🗑")
                await send_message.add_reaction("⏹")
                await send_message.add_reaction("➡")

            if page_count == 2:
                await send_message.add_reaction("⬅")
                await send_message.add_reaction("🗑")
                await send_message.add_reaction("⏹")
                await send_message.add_reaction("➡")

            if page_count == 3:
                await send_message.add_reaction("⬅")
                await send_message.add_reaction("🗑")
                await send_message.add_reaction("⏹")
                
@bot.command(aliases=["url","link"],description=f"Starry Skyの招待リンクを送信するよ。")
async def invite(ctx):
    return await ctx.send("https://discord.com/api/oauth2/authorize?client_id=797378859199627284&permissions=4228906231&scope=bot")

@bot.command(aliases=["git"],description="Githubのリンクを表示するよ。")
@commands.is_owner()
async def github(ctx):
    return await ctx.send("https://github.com/Mr-ShiRoNo/Starry-Sky")

@bot.command(aliases=["adm"],description="BOTの管理者達を表示するよ。")
async def admins(ctx):
    e=discord.Embed(title="BOT管理者",description="StarSkyの管理者達だよ。",color=0x03a9fc)
    e.add_field(name="**__オーナー__**",value=f"{bot.get_user(584008752005513216).name}",inline=False)
    e.add_field(name="**__サブオーナー__**",value="\n".join(bot.get_user(s).name for s in subowner),inline=False)
    e.add_field(name="**__管理者__**",value="\n".join(bot.get_user(s).name for s in admin),inline=False)
             
    await ctx.send(embed=e)

@bot.command(aliases=["rolei","ri"],description="指定した役職の情報を表示するよ。\n※役職IDでやるのがいいよ。")
async def roleinfo(ctx, *, role:discord.Role):
    e = discord.Embed(title=f"役職情報 - {role.name}", description="",color=ctx.author.color,timestamp=datetime.datetime.utcnow())
    e.add_field(name="名前", value=role.name)
    e.add_field(name="ID", value=role.id)
    e.add_field(name="所属サーバー", value=role.guild.name+f"({role.guild.id})")
    e.add_field(name="他のメンバーと別に表示するか？", value=role.hoist)
    e.add_field(name="その他サービスによって管理されているか？", value=role.managed)
    e.add_field(name="メンション可能か？", value=role.mentionable)
    e.add_field(name="役職順位(一番下を0としたとき)", value=role.position)
    e.add_field(name="役職の色", value=role.color)
    e.add_field(name="役職作成日(UTC)", value=role.created_at)
    e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
    await ctx.send(embed=e)
    
@bot.command(aliases=["chinfo","chi","ci"],description="指定したチャンネルの情報を表示するよ。")
async def channelinfo(ctx, *, channelid=None):
        if channelid == None:
            e = discord.Embed(title="チャンネル情報",color=ctx.author.color,timestamp=datetime.datetime.utcnow())
            e.add_field(name="チャンネル名", value=ctx.channel.name)
            e.add_field(name="チャンネルID", value=ctx.channel.id)
            e.add_field(name="所属サーバー", value=ctx.channel.guild.name+f"({ctx.channel.guild.id})")
            e.add_field(name="トピック", value=ctx.channel.topic)
            e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
            await ctx.send(embed=e)

        else:
            try:
                await bot.wait_until_ready()
                channel = bot.get_channel(channelid)

                e = discord.Embed(title="チャンネル情報", description="",color=ctx.author.color,timestamp=datetime.datetime.utcnow())
                e.add_field(name="チャンネル名", value=channel.name)
                e.add_field(name="チャンネルID", value=channel.id)
                e.add_field(name="所属サーバー", value=channel.guild.name+f"({channel.guild.id})")
                e.add_field(name="トピック", value=channel.topic)
                e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
                await ctx.send(embed=e)
            except Exception:
                try:
                    await bot.wait_until_ready()
                    channel = await bot.fetch_channel(channelid)

                    e = discord.Embed(title="チャンネル情報", description="",color=ctx.author.color,timestamp=datetime.datetime.utcnow())
                    e.add_field(name="チャンネル名", value=channel.name)
                    e.add_field(name="チャンネルID", value=channel.id)
                    e.add_field(name="所属サーバー", value=channel.guild.name+f"({channel.guild.id})")
                    e.add_field(name="トピック", value=channel.topic)
                    e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
                    await ctx.send(embed=e)

                except discord.NotFound:
                    e = discord.Embed(title="チャンネル情報", description="指定されたチャンネルは存在しません。")
                    await ctx.send(embed=e)

                except discord.Forbidden:
                    e = discord.Embed(title="チャンネル情報", description="指定されたチャンネルへアクセスできませんでした。")
                    await ctx.send(embed=e)
                    
@bot.command(aliases=["usearch","use"],description="指定したユーザーの情報を表示するよ。\nサーバーに居ない人の情報も検索できるね。\nでもID限定、表示できる情報がuserinfoより少ないよ")
async def usersearch(ctx, user_id=""):
    
    try:user = await bot.fetch_user(int(user_id))
    except:await ctx.send(embed=discord.Embed(description="ユーザーが見つかりませんでした…。",color=ctx.author.color))
    else:
        embed = discord.Embed(title=f"ユーザーサーチ - {user.name}",color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'{user.avatar_url_as(static_format="png")}')
        embed.add_field(name="名前#タグ",value=f"{user}", inline=False)
        embed.add_field(name="ID",value=f"{user.id}", inline=False)
        embed.add_field(name="BOT?",value={"True":"はい","False":"いいえ"}.get(str(user.bot)), inline=False)
        embed.add_field(name="アカウント作成日",value=f"{user.created_at.strftime('%Y年%m月%d日 %H時%M分%S秒')}", inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
        await ctx.send(embed=embed)
                        
@bot.command(aliases=["useri","ui"],description="指定したユーザーの情報を表示するよ。\n引数なしの場合、実行者の情報が表示されるよ。")
async def userinfo(ctx, *, user: discord.Member=None):
    embed=discord.Embed(title="ユーザー情報 - 検索中・・・",description="ユーザーを検索しているよ・・・\nしばらく待ってね・・・",color=0x03a9fc)
    embed.set_footer(text="User Searching Now...")
    msg = await ctx.send(embed=embed)
    if user == None:
        embed = discord.Embed(title=f"ユーザー情報 - {ctx.author.name}",color=ctx.author.color,timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'{ctx.author.avatar_url_as(static_format="png")}')
        embed.add_field(name="名前#タグ",value=f"{ctx.author}")
        embed.add_field(name="ID",value=f"{ctx.author.id}")
        embed.add_field(name=f"ステータス({s.ondevicon(ctx.author)})",value={"online":"オンライン","idle":"退席中","dnd":"取り込み中","offline":"オフライン"}.get(str(ctx.author.status)))
        embed.add_field(name="BOT?",value={"True":"はい","False":"いいえ"}.get(str(ctx.author.bot)))
        if not ctx.author.activity == None:
            try:
                if ctx.author.activity.type == discord.ActivityType.custom:
                    embed.add_field(name="アクティビティ", value=ctx.author.activity)
                else:
                    embed.add_field(name="アクティビティ", value=ctx.author.activity.name)
            except:
                embed.add_field(name="アクティビティ", value=ctx.author.activity)
        embed.add_field(name="サーバー上の名前", value=ctx.author.display_name)
        embed.add_field(name="サーバー参加時間",value=f"{ctx.author.joined_at.strftime('%Y年%m月%d日 %H時%M分%S秒')}")
        embed.add_field(name="アカウント作成日",value=f"{ctx.author.created_at.strftime('%Y年%m月%d日 %H時%M分%S秒')}")
        if len(ctx.author.roles) <= 1000:embed.add_field(name="役職",value=",".join(c.mention for c in list(reversed(ctx.author.roles))), inline=False)
        else:embed.add_field(name="役職",value='多すぎて表示できないよ。', inline=False)
        embed.add_field(name=f"権限 - {ctx.author.guild_permissions.value}", value=",".join("`{}`".format(bot.json_config["roles"].get(c, str(c))) for c,b in dict(ctx.author.guild_permissions).items() if b is True))
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")

        await msg.edit(embed=embed)
    else:
        embed = discord.Embed(title=f"ユーザー情報 - {user.name}",color=user.color,timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'{user.avatar_url_as(static_format="png")}')
        embed.add_field(name="名前#タグ",value=f"{user}")
        embed.add_field(name="ID",value=f"{user.id}")
        embed.add_field(name=f"ステータス({s.ondevicon(user)})",value={"online":"オンライン","idle":"退席中","dnd":"取り込み中","offline":"オフライン"}.get(str(user.status)))
        embed.add_field(name="BOT?",value={"True":"はい","False":"いいえ"}.get(str(user.bot)))
        if not user.activity == None:
            try:
                if user.activity.type == discord.ActivityType.custom:
                    embed.add_field(name="アクティビティ", value=user.activity)
                else:
                    embed.add_field(name="アクティビティ", value=user.activity.name)
            except:
                embed.add_field(name="アクティビティ", value=user.activity)
        embed.add_field(name="サーバー上の名前", value=user.display_name)
        embed.add_field(name="サーバー参加時間",value=f"{user.joined_at.strftime('%Y年%m月%d日 %H時%M分%S秒')}")
        embed.add_field(name="アカウント作成日",value=f"{user.created_at.strftime('%Y年%m月%d日 %H時%M分%S秒')}")
        if len(user.roles) <= 1000:embed.add_field(name="役職",value=",".join(c.mention for c in list(reversed(user.roles))), inline=False)
        else:embed.add_field(name="役職",value='多すぎて表示できないよ。', inline=False)
        embed.add_field(name=f"権限 - {user.guild_permissions.value}", value=",".join("`{}`".format(bot.json_config["roles"].get(c, str(c))) for c,b in dict(user.guild_permissions).items() if b is True))
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")

        await msg.edit(embed=embed)

@bot.command(aliases=["serveri","si"],description="指定したサーバーの情報を表示するよ。\n※サーバーIDでやってね。")
async def serverinfo(ctx,guild_id=None):
    if guild_id == None:
        ch_tcount =len(ctx.guild.text_channels)
        ch_vcount =len(ctx.guild.voice_channels)
        ch_count =len(ctx.guild.channels)
        kt_count =len(ctx.guild.categories)
        embed = discord.Embed(title=f"サーバー情報 - {ctx.guild.name}",color=ctx.author.color)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name="名前",value=f"{ctx.guild.name}")
        embed.add_field(name="ID",value=f"{ctx.guild.id}")
        embed.add_field(name="サーバー地域",value=f"{ctx.guild.region}")
        embed.add_field(name="作成日",value=f"{ctx.guild.created_at}")
        embed.add_field(name="オーナー",value=f"{ctx.guild.owner}")
        embed.add_field(name="テキストチャンネル数",value=f"{ch_tcount}")
        embed.add_field(name="ボイスチャンネル数",value=f"{ch_vcount}")
        embed.add_field(name="カテゴリー数",value=f"{kt_count}")
        embed.add_field(name="合計チャンネル数(カテゴリー含む)",value=f"{ch_count}")
        embed.add_field(name="サーバー承認レベル",value=f"{ctx.guild.mfa_level}")
        embed.add_field(name="サーバー検証レベル",value=f"{ctx.guild.verification_level}")
        embed.add_field(name="サーバーブーストレベル",value=f"{ctx.guild.premium_tier}")
        embed.add_field(name="サーバーをブーストしたユーザー数",value=f"{ctx.guild.premium_subscription_count}")
        embed.add_field(name="サーバーは大きい？",value=f"{ctx.guild.large}")
        embed.set_footer(text="サーバー大きさ基準:250人以上")

        await ctx.send(embed=embed)
    else:
        guild = bot.get_guild(int(guild_id))
        ch_tcount =len(guild.text_channels)
        ch_vcount =len(guild.voice_channels)
        ch_count =len(guild.channels)
        kt_count =len(guild.categories)
        guild = discord.utils.get(bot.guilds,id=int(guild_id))
        embed = discord.Embed(title=f"サーバー情報 - {guild.name}",color=ctx.author.color)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="名前",value=f"{guild.name}")
        embed.add_field(name="ID",value=f"{guild.id}")
        embed.add_field(name="サーバー地域",value=f"{guild.region}")
        embed.add_field(name="作成日",value=f"{guild.created_at}")
        embed.add_field(name="オーナー",value=f"{guild.owner}")
        embed.add_field(name="テキストチャンネル数",value=f"{ch_tcount}")
        embed.add_field(name="ボイスチャンネル数",value=f"{ch_vcount}")
        embed.add_field(name="カテゴリー数",value=f"{kt_count}")
        embed.add_field(name="合計チャンネル数(カテゴリー含む)",value=f"{ch_count}")
        embed.add_field(name="サーバー承認レベル",value=f"{guild.mfa_level}")
        embed.add_field(name="サーバー検証レベル",value=f"{guild.verification_level}")
        embed.add_field(name="サーバーブーストレベル",value=f"{guild.premium_tier}")
        embed.add_field(name="サーバーをブーストしたユーザー数",value=f"{guild.premium_subscription_count}")
        embed.add_field(name="サーバーは大きい？",value=f"{guild.large}")
        embed.set_footer(text="サーバー大きさ基準:250人以上")

        await ctx.send(embed=embed)
                        
@bot.command(aliases=["joinserverl","joins"],description="Botが導入されているサーバーを表示するよ。")
async def joinserverlist(ctx):
    await ctx.send(embed=discord.Embed(title="導入されているサーバー一覧",description="\n".join([guild.name for guild in bot.guilds]),color=col))                       
##### 一般ユーザー系コマンド #####
                        
@bot.command(description="BOTの反応速度を測定するよ。")
async def ping(ctx):
    msg = await ctx.send("測定中...")
    times = (msg.created_at - ctx.message.created_at).microseconds // 1000
    des = f"Rate:`{times}ms`\nLatency:`{round(bot.latency * 1000)}ms`"
    await msg.edit(content=None,embed=discord.Embed(title="Pong!",description=des,color=bcol))

@bot.command(aliases=["cview"],description="指定した色のembedを生成するよ。\n色を確かめたい時などに活用してね。(RGB)")
async def colorview(ctx,r:int,g:int,b:int):
    color=discord.Colour.from_rgb(r,g,b)
    e=discord.Embed(title=f"{r},{g},{b}",color=color)
    await ctx.send(embed=e)
                        
@bot.command(aliases=["uico"],description="指定したユーザーのアイコンを表示するよ。\n引数がない場合、実行者のアイコンが表示されるよ。")
async def usericon(ctx,*,user:discord.Member=None):
    if user is None:
        e=discord.Embed(title=f"{ctx.author.name}さんのアイコン",color=ctx.author.color)
        e.set_image(url=ctx.author.avatar_url_as(static_format="png"))
        await ctx.send(embed=e)
    else:
        e=discord.Embed(title=f"{user.name}さんのアイコン",color=user.color)
        e.set_image(url=user.avatar_url_as(static_format="png"))
        await ctx.send(embed=e)
                        
@bot.command(aliases=["btime"],description="BOTの稼働時間を表示するよ。")
async def boottime(ctx):
    e=discord.Embed(title=f"{bot.user.name}の稼働時間",color=bcol)
    e.add_field(name="起動した時刻",value=uptime.boottime().strftime("%Y年%m月%d日 %H時%M分%S秒"),inline=False)
    e.add_field(name="起動してから",value=f"{uptime.uptime()}秒",inline=False)
    await ctx.send(embed=e)
##### メッセージ #####
                        
@bot.command(aliases=["dmsend"],description="指定したユーザーに僕からDMを送信するよ。\n`BOTサブオーナーとBOT運営`しか使用できないね。。")
async def senddm(ctx, userid, desc=None):
    try:
        if ctx.author.id in admin or ctx.author.id in subowner or ctx.author.id == 584008752005513216 or 751653229112328283:
            user = await bot.fetch_user(userid)
            e = discord.Embed(description=desc,color=0x03a9fc,timestamp=datetime.datetime.utcnow())
            e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
            await user.send(embed=e)

            c = discord.Embed(title="DM送信", description=f"{user.mention}にDMを送信したよ。",color=ctx.author.color)
            e.set_footer(icon_url=ctx.author.avatar_url,text=f"実行者:{ctx.author}")
            await ctx.send(embed=c)
        else:
            await ctx.send(embed=discord.Embed(title="実行エラー",description="あなたはBOT管理者じゃないよ。",color=0xff0000))            
                        

    except discord.NotFound:
        e = discord.Embed(title="DM送信", description="指定されたユーザーは存在しないよ。",color=0xff0000)
    
    except discord.Forbidden:
        e = discord.Embed(title="DMメッセージ送信", description="指定されたユーザーにDMを送信できなかったよ。",color=0xff0000)
        await ctx.send(embed=e)
                        
@bot.command(aliases=["ssenddm","dmssend"],description="指定したユーザーになつからDMを送信するよ。\n送信者の名前は隠されるよ。\n製作者しか使えないね。")
@commands.is_owner()
async def secretsenddm(ctx, userid, desc=None):
    try:
        user = await bot.fetch_user(userid)
        e = discord.Embed(description=desc,color=0x03a9fc,timestamp=datetime.datetime.utcnow())
        e.set_footer(text="実行者:Starry Sky")
        await user.send(embed=e)

        c = discord.Embed(title="シークレットDM送信", description=f"{user.mention}にDMを送信したよ。",color=ctx.author.color)
        e.set_footer(text="実行者:Starry Sky")
        await ctx.send(embed=c)

    except discord.NotFound:
        e = discord.Embed(title="シークレットDM送信", description="指定されたユーザーは存在しないよ。",color=0xff0000)
    
    except discord.Forbidden:
        e = discord.Embed(title="シークレットDM送信", description="指定されたユーザーにDMを送信できなかったよ。",color=0xff0000)
        await ctx.send(embed=e)
                        
@bot.command(description="指定した文章を送信するよ。")
async def say(ctx, *, message:discord.ext.commands.clean_content()):
    await ctx.send(message)
    await ctx.message.delete()
                        
@bot.command(description="指定したチャンネルに文章を送信するよ。\n`BOTサブオーナーとBOT運営`しか使用できないね。")
async def send(ctx, ch:discord.TextChannel, txt:discord.ext.commands.clean_content()):
    try:
        if ctx.author.id in admin or ctx.author.id in subowner or ctx.author.id == 584008752005513216 or 751653229112328283:
            await ch.send(txt)

            e = discord.Embed(title="メッセージ送信", description=f"{ch.mention}に{txt}を送信しました。",color=ctx.author.color)
            await ctx.send(embed=e)
        else:
            await ctx.send(embed=discord.Embed(title="実行エラー",description="あなたはBOT管理者じゃないよ。",color=0xff0000))

    except discord.NotFound:
        e = discord.Embed(title="メッセージ送信", description="指定されたチャンネルが存在しないよ。",color=0xff0000)
        await ctx.send(embed=e)
    except discord.Forbidden:
        e = discord.Embed(title="メッセージ送信", description="指定されたチャンネルにアクセスできないよ。",color=0xff0000)
        await ctx.send(embed=e)
##### 計算 #####
                        
@bot.command(aliases=["calc"],description="計算をするよ。\n※`eval`と同じコードだけど、評価はできないよ。")
async def math(ctx,*,siki:discord.ext.commands.clean_content()):
    try:
        e=discord.Embed(description="**計算中・・・**",color=0x03a9fc)
        msg = await ctx.send(embed=e)
        if "token" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "os" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "exec" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "eval" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "TOKEN" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "globals" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="**{result}**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "ctx" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "await" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "client" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "self" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "bot" in siki:
            if ctx.message is not None:await ctx.message.add_reaction("‼")
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return
        if "print" in siki:
            e=discord.Embed(description="❌** | evalはできないよ。**",color=0x03a9fc)
            await msg.edit(embed=e)
            return    
        result = eval(siki)
        e=discord.Embed(description=f"**{result}**",color=0x03a9fc)
        await msg.edit(embed=e)
    except SyntaxError:
        e=discord.Embed(description="❌** | 不正な式だよ。**",color=0x03a9fc)
        await msg.edit(embed=e)
    except NameError:
        e=discord.Embed(description="❌** | 不正な式だよ。**",color=0x03a9fc)
        await msg.edit(embed=e)
    except TypeError:
        e=discord.Embed(description="❌** | 不正な式だよ。**",color=0x03a9fc)
        await msg.edit(embed=e)
    except discord.HTTPException:
        e=discord.Embed(description="❌** | 計算結果が2000文字を超えているよ。**",color=0x03a9fc)
        await msg.edit(embed=e)
##### 遊び #####
                        
@bot.command(aliases=["mkembed"],description="embed(埋め込み表示)を作成するよ。\色は実行者の名前の色になるよ。")
async def makeembed(ctx, title, *, word):
    e = discord.Embed(title=title, description=word, color=ctx.author.color)
    await ctx.send(embed=e)
                        
@bot.command(aliases=["randomnum","rnum"],description="ランダムな数(乱数)を出すよ。")
async def randomnumber(ctx, startnum:int, endnum:int):
    randomnumgen = random.randint(startnum, endnum)
    await ctx.send(randomnumgen)
                        
@bot.command(description="サイコロを振るよ。")
async def dice(ctx):
    dicenum = random.randint(0, 6)
    await ctx.send(dicenum)
                        
@bot.command(description="おみくじを引くよ。")
async def omikuji(ctx):
    embed = discord.Embed(title="おみくじ", description=f"{ctx.author.mention}さんの今日の運勢は。\nｼﾞｬｶｼﾞｬｶｼﾞｬｶｼﾞｬｶｼﾞｬｶ…ｼﾞｬﾝ!",color=0x03a9fc)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="[運勢] ", value=random.choice(('福沢諭吉\nお！福沢ゆきｔ・・・え？(笑)','大吉。\nすごいね。大吉だよ？。', '吉\nいいね。', '凶\nそんなこともあるさ。', '大凶\nあ、ありゃりゃ・・・')), inline=False)
    await ctx.send(embed=embed)
                        
@bot.command(aliases=["vote"],description="投票を作成するよ。\n最大20個まで作成可能。")
async def poll(ctx,*content):
    if len(content) == 1:
        msg = await ctx.send(content[:1][0])
        [await msg.add_reaction(emoji) for emoji in ["👍","👎"]]
    elif len(content) > 1:
        title = content[:1][0]
        answers = content[1:]
        emojis = [chr(127462 + i) for i in range(len(answers))]
        answer = "\n".join(emoji + answer for emoji,answer in zip(emojis,answers))
        col = random.randint(0, 0xFFFFFF)
        embed = discord.Embed(title=f"📊**__{title}__**",description=answer,color=col,timestamp=datetime.datetime.utcnow())
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"作成者:{ctx.author.name}")
        msg = await ctx.send(embed=embed)
        [await msg.add_reaction(emoji) for emoji in emojis]

##### ログ #####
@bot.event
async def on_member_join(member):
    print(f'{member}さんが{member.guild}に参加しました。')
                        
@bot.event
async def on_member_remove(member):
    print(f'{member}さんが{member.guild}から退出しました。')

##### エラー系コード #####
@bot.event
async def on_command_error(context,exception):
    if isinstance(exception, commands.CommandNotFound):
        word = context.message.content.split(" ")[0].strip("s!")
        des = ",".join(c.name for c in bot.commands if word in c.name or c.name in word)
        embed = discord.Embed(title="コマンドエラー",description=f"{context.author.name}さん、`{context.message.content}`っていうコマンドは無いよ。\n`s!help`で確認してね。\nもしかして:`{des}`\n※`もしかして`が機能しないこともあるよ。", color=0xff0000)
        await context.send(embed=embed)
        print (f"[StarSky System] コマンド名エラー:『{context.message.content}』を{context.message.author}さんが間違えました。\nサーバー:{context.message.guild}")
    elif isinstance(exception, commands.MissingRequiredArgument):
        await context.send(embed=discord.Embed(title="コマンドエラー - 引数不足",description="コマンドのパラメーターが不足しているよ。",color=0xff0000))
        print (f"[StarSky System] コマンドパラメーターエラー:『{context.message.content}』を{context.message.author}さんが間違えました。\nサーバー:{context.message.guild}")
    elif isinstance(exception,commands.NotOwner):
        await context.send(embed=discord.Embed(title="実行エラー - オーナーコマンド",description="あなたはBOTオーナーじゃないよ。",color=0xff0000))
        print (f"[StarSky System] オーナー専用コマンド実行:『{context.message.content}』を{context.message.author}さんが実行しました。\nサーバー:{context.message.guild}")
    elif isinstance(exception, commands.DisabledCommand):
        embed = discord.Embed(title="コマンドエラー", description="そのコマンドは無効化されてるよ。", color=0xff0000)
        await context.send(embed=embed)
    elif isinstance(exception, commands.BotMissingPermissions):
        embed = discord.Embed(title="権限エラー", description="`BOT`に権限がないから、コマンドを実行できないよ。", color=0xff0000)
        await context.send(embed=embed)
    else:
        e = discord.Embed(title="‼Exception Occurred‼", description=f"例外が発生しました。\n```\n{exception}\n```", color=0xff0000)
        print (f"[StarSky System] 例外が発生しました。\n『{exception}』\n発生サーバー:{context.message.guild}\n発生ユーザー:{context.message.author}")
        await context.send(embed=e)

##### その他のコード #####
#現在無し
##### ヘルプ #####
@bot.command(description="制作者用コマンドヘルプを表示するよ。\nBOT製作者しか使えないよ。")
@commands.is_owner()
async def helpowner(ctx):
    e = discord.Embed(title="Command Help Owner - コマンドヘルプ",description="コマンドの先頭には、必ず`s!`がいるよ。。",color=0x03a9fc)
    e.add_field(name="Debug commands/デバッグコマンド",value="`command`,`remove`,`eval`,`valu`,`evalfree`,`reboot`,`down`,`shell`,`jishaku`",inline=False)
    e.add_field(name="Message commands/メッセージコマンド",value="`send`,`senddm`,`secretsenddm`,`github`",inline=False)
    e.add_field(name="Status&Activity commands/ステータス&アクテビティコマンド",value="`setactivity`,`resetactivity`,`setonline`,`setidle`,`setdnd`",inline=False)
    e.add_field(name="Other/その他のコマンド",value="`leaveguild`",inline=False)
    
    await ctx.send(embed=e)
                    
@bot.command(description="コマンドヘルプを表示するよ。\n引数にコマンド名を入れると、そのコマンドのヘルプが表示されるよ。\n引数はあってもなくてもOK。")
async def help(ctx,name=None):
    if name is not None:
        if [c for c in bot.commands if c.name == name or name in c.aliases]:
            command = [c for c in bot.commands if c.name == name or name in c.aliases][0]
            embed = discord.Embed(title=f"コマンド: `{command.name}` - ヘルプ",color=0x03a9fc)
            if command.description:embed.add_field(name="説明",value=command.description,inline=False)
            else:embed.add_field(name="説明",value="説明はないよ",inline=False)        
            embed.add_field(name="名前",value=command.name)
            if command.aliases:embed.add_field(name="エイリアス",value="`{}`".format(",".join(c for c in command.aliases)))
            else:embed.add_field(name="エイリアス",value="エイリアスはないよ",)
            embed.add_field(name="コマンドタイプ",value=command.__class__.__name__,inline=False)
            embed.add_field(name="使い方",value=f"`s!{command.name} {((' '.join(f'[{c}]' for c in command.clean_params.keys())) if len(command.clean_params) > 0 else '')}`",inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Command Help - Error",description=f"『{name}』っていうコマンドは存在しないよ。\n`s!help`で確認してね。", color=0xff0000)
            await ctx.send(embed=embed)
    else:
        fist = discord.Embed(title="全コマンド一覧",description=f"計{len(bot.commands)}コマンドの一覧だよ。(管理者専用コマンド含む)",color=0x03a9fc)
        fist.add_field(name="注意",value="・BOTに付与されている役職の位置により、使用できないコマンドがある可能性があります。\n・権限不足により、実行できないコマンドがあります。(権限を付与すれば解決します。)\n・`※`がついているコマンドは使用前に詳細ヘルプを見てください。\n・20秒リアクションを押さずに放置すると、ページが使用できなくなります。",inline=False)
        fist.add_field(name="詳細ヘルプの見方",value="`s!help`の後に詳細を見たいコマンド名を入力すると、そのコマンドの使い方や説明などが見れます。\n例:`s!help info`")
        fist.add_field(name="ページの操作方法",value="➡:次のページに進むよ。\n⬅:前にページに戻るよ。\n🗑:このメッセージを削除するよ。\n⏹:このメッセージを表示したまま処理を停止するよ。",inline=False)
        fist.set_footer(text="HelpPage(1/9)")
        e1 = discord.Embed(title="ボット情報系コマンド",description="`info`,`help`,`ping`,`joinserverlist`,`invite`",color=0x03a9fc)
        e1.set_footer(text="HelpPage(2/9)")
        e2 = discord.Embed(title="一般ユーザー向けコマンド",description="Message:`makeembed`,`say`,`messagehistory`\nVote:`poll`\nPlay:`randomnumber`,`dice`,`omikuji`\nCalculation:`math`",color=0x03a9fc)
        e2.set_footer(text="HelpPage(3/9)")
        e3 = discord.Embed(title="報告コマンド",description="`なし`",color=0x03a9fc)
        e3.set_footer(text="HelpPage(4/9)")
        e4 = discord.Embed(title="情報コマンド",description="`userinfo`,`usersearch`,`serverinfo`,`roleinfo`,`channelinfo`,`boottime`,`usericon`",color=0x03a9fc)
        e4.set_footer(text="HelpPage(5/9)")
        e5 = discord.Embed(title="役職コマンド",description="`rolecreat`,`roledelete`,`roleadd`,`roleremove`,`roleusers`,`rolecolor`,`roleallmembersadd`,`roleallmembersremove`",color=0x03a9fc)
        e5.set_footer(text="HelpPage(6/9)")
        e6 = discord.Embed(title="サーバー管理コマンド",description="User:`ban`,`kick`\nMessage:`clear`,`※allclear`\nChannel:`textchannelcreate`,`textchanneldelete`,`voicechannelcreate`,`voicechanneldelete`,`channeledit`,\nCategory:`categorycreate`,`categorydelete`",color=0x03a9fc)
        e6.set_footer(text="HelpPage(7/9)")
        e7 = discord.Embed(title="その他のコマンド",description=f"`admins`,`colorview`",color=0x03a9fc)
        e7.set_footer(text="HelpPage(8/9)")
        e8 = discord.Embed(title="BOT管理者専用コマンド",description="`eval`,`valu`,`setactivity`,`resetactivity`,`setonline`,`setidle`,`setdnd`,`send`,`senddm`",color=0x03a9fc)
        e8.set_footer(text="HelpPage(9/9)")
        page_count = 0 #ヘルプの現在表示しているページ数
        page_content_list = [fist, e1, e2, e3, e4 ,e5, e6, e7,e8] #ヘルプの各ページ内容
        send_message = await ctx.send(embed=page_content_list[0]) #最初のページ投稿
        await send_message.add_reaction("➡")
        await send_message.add_reaction("🗑")
        await send_message.add_reaction("⏹")

        def help_react_check(reaction,user):
            emoji = str(reaction.emoji)
            if reaction.message.id != send_message.id:
                return 0
            if emoji == "➡" or emoji == "⬅" or emoji == "🗑" or emoji == "⏹":
                if user != ctx.author:
                    return 0
                else:
                    return 1
        while not bot.is_closed():
            try:
                reaction,user = await bot.wait_for('reaction_add',check=help_react_check,timeout=30.0)
            except asyncio.TimeoutError:
                await send_message.clear_reactions()
                await send_message.add_reaction("❌")
                return #時間制限が来たら、それ以降は処理しない
            else:
                emoji = str(reaction.emoji)
                if emoji == "➡":
                    page_count += 1
                if emoji == "⬅":
                    page_count -= 1
                if emoji == "⏹":
                    await send_message.clear_reactions()
                    await send_message.add_reaction("❌")
                    return
                if emoji == "🗑":
                    return await send_message.delete()
                await send_message.clear_reactions() #事前に消去する
                await send_message.edit(embed=page_content_list[page_count])

                if page_count == 0:
                    await send_message.add_reaction("➡")
                    await send_message.add_reaction("🗑")
                    await send_message.add_reaction("⏹")

                if page_count == 1:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("🗑")
                    await send_message.add_reaction("⏹")
                    await send_message.add_reaction("➡")

                if page_count == 2:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("🗑")
                    await send_message.add_reaction("⏹")
                    await send_message.add_reaction("➡")

                if page_count == 3:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("🗑")
                    await send_message.add_reaction("⏹")
                    await send_message.add_reaction("➡")

                if page_count == 4:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("🗑")
                    await send_message.add_reaction("⏹")
                    await send_message.add_reaction("➡")
            
                if page_count == 5:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("🗑")
                    await send_message.add_reaction("⏹")
                    await send_message.add_reaction("➡")

                if page_count == 6:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("🗑")
                    await send_message.add_reaction("⏹")
                    await send_message.add_reaction("➡")

                if page_count == 7:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("🗑")
                    await send_message.add_reaction("⏹")
                    await send_message.add_reaction("➡")
                            
                if page_count == 8:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("🗑")
                    await send_message.add_reaction("⏹")

token = os.environ['DISCORD_BOT_TOKEN']             
bot.run(token)
