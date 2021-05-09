import discord.ext 
from discord.ext import commands

#権限不足
async def no_per(ctx,per,color):
    if per == "channel":
        e=discord.Embed(title="権限不足",description="君は`チャンネルを管理する権限`を持ってないよ。",color=color)
        await ctx.send(embed=e)
    elif per == "role":
        e=discord.Embed(title="権限不足",description="君は`役職を管理する権限`を持ってないよ。",color=color)
        await ctx.send(embed=e)
    elif per == "server":
        e=discord.Embed(title="権限不足",description="君は`サーバーを管理する権限`を持ってないよ。",color=color)
        await ctx.send(embed=e)
    elif per == "message":
        e=discord.Embed(title="権限不足",description="君は`メッセージを管理する権限`を持ってないよ。",color=color)
        await ctx.send(embed=e)
    elif per == "emoji":
        e=discord.Embed(title="権限不足",description="君は`絵文字を管理する権限`を持ってないよ。",color=color)
        await ctx.send(embed=e)
    elif per == "kick":
        e=discord.Embed(title="権限不足",description="君は`ユーザーをkickする権限`を持ってないよ。",color=color)
        await ctx.send(embed=e)
    elif per == "ban":
        e=discord.Embed(title="権限不足",description="君は`ユーザーをbanする権限`を持ってないよ。",color=color)
        await ctx.send(embed=e)
    else:
        await ctx.send("あなたは権限不足のため、コマンドを実行できません。")
        
#アイコン取得   
def ondevicon(mem):
    tmp = ""
    if not str(mem.mobile_status) == "offline":
        tmp = tmp+"📱"
    if not str(mem.web_status) == "offline":
        tmp = tmp+"🌐"
    if not str(mem.desktop_status) == "offline":
        tmp = tmp+"💻"
    return tmp

#BOTでの運営またはサブオーナーではない
async def no_admin(ctx,adm,color):
    if adm == "admin":
        e=discord.Embed(title="権限不足",description="君は`BOT運営`じゃないよ。",color=color)
        await ctx.send(embed=e)
    elif adm == "subowner":
        e=discord.Embed(title="権限不足",description="君は`BOTサブオーナー`じゃないよ。",color=color)
        await ctx.send(embed=e)
    elif adm == "owner":
        e=discord.Embed(title="権限不足",description="君は`BOTオーナー`じゃないよ。",color=color)
        await ctx.send(embed=e)
