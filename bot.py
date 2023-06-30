import discord
import asyncio

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "同意":
        global memids
        global isApprove
        if str(message.author.id) not in memids:
            await message.reply("你又不在頻道裡面，同意你媽")
        else:
            await message.reply("好啦幹，叫他不要吵")
            isApprove = True

@client.event
async def on_voice_state_update(member, before, after):
    if member.id != 579301620144275457:
        return
    waiting_room = client.get_channel(1124331819953831956)
    member1 = member
    if after.channel == waiting_room:
        target_channel = client.get_channel(1083026174084665455)
        mentionmembers = target_channel.members
        global memids
        memids = ""
        for member in mentionmembers:
            memids = memids + (" <@" + str(member.id) + ">")
        await client.get_channel(1014183513823641610).send(memids +  "OOO進入了等待頻道，是否同意進入?")
        global isApprove
        isApprove = False
        times = 0
        while True:
            times = times + 1
            if isApprove:
                await member1.move_to(target_channel)
                isApprove = False
                break
            if times > 30:
                await client.get_channel(1014183513823641610).send("沒有，沒有，沒有，沒有，沒有，沒有，沒有")
                await client.get_channel(1014183513823641610).send("不通過")
                break
            await asyncio.sleep(1)

client.run("TOKEN")
