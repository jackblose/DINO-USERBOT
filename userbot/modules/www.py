# Copyright (C) 2019 The Raphielscape Company LLC.
# RAM-UBOT MINTA
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import time
import redis

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^Sping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Sabar.__")
    await pong.edit("__Sabar..__")
    await pong.edit("__Sabar...__")
    await pong.edit("__Sabar....__")
    await pong.edit("__Bentar.__")
    await pong.edit("__Bentar..__")
    await pong.edit("__Bentar...__")
    await pong.edit("__Bentar....__")
    await pong.edit("__Nah!!__")
    await pong.edit("๐ฅ")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**โญโโโโโโโโโโโโโโโโโโฎ** \n"
                    f"**        ๐ฅ แดษชษดแด-แดsแดสสแดแด ๐ฅ** \n"
                    f"**  โ?โผโโโโโโโโโโโโโโโ?** \n"
                    f"**        โข sษชษขษดแดส  :** `%sms` \n"
                    f"**        โข แดแดกษดแดส   :** `{ALIVE_NAME}` \n"
                    f"**        โข สแดแด แด?แดส  :** `7.0` \n"
                    f"**โฐโโโโโโโโโโโโโโโโโโฏ** \n" % (duration))


@register(outgoing=True, pattern="^Lping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting to server...`")
    await pong.edit("โ?๏ธ")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**`{ALIVE_NAME}`**\n"
                    f"โง **-แดษชษดแด-แดsแดสสแดแด- :** "
                    f"`%sms` \n"
                    f"โง **-แดแดแดษชแดแด- :** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Xping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Mohon menunggu.__")
    await pong.edit("__Mohon menunggu..__")
    await pong.edit("__Mohon menunggu...__")
    await pong.edit("__Mohon menunggu.__")
    await pong.edit("__Mohon menunggu..__")
    await pong.edit("__Mohon menunggu...__")
    await pong.edit("__Mohon menunggu.__")
    await pong.edit("__Mohon menunggu..__")
    await pong.edit("__Mohon menunggu...__")
    await pong.edit("๐")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"โญโ?โผโโโโโโโโโโโโโโโ?โฎ\n"
                    f"โฃ[โข**PONG!!**\n"
                    f"โฃ[โข__Signal__    __:__ "
                    f"`%sms` \n"
                    f"โฃ[โข__Uptime__ __:__ "
                    f"`{uptime}` \n"
                    f"โฐโ?โผโโโโโโโโโโโโโโโ?โฏ\n" % (duration))


@register(outgoing=True, pattern="^Ping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Ping.__")
    await pong.edit("__Pong..__")
    await pong.edit("__Ping...__")
    await pong.edit("__Pong....__")
    await pong.edit("__Ping.__")
    await pong.edit("__Pong..__")
    await pong.edit("__Ping...__")
    await pong.edit("__Pong....__")
    await pong.edit("๐ฅ")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**โญโ?โผโโโโโโโโโโโโโโโ?โฎ**\n"
                    f"**            ๐ฅแดษชษดแด-แดsแดสสแดแด๐ฅ**\n"
                    f"**โฐโ?โผโโโโโโโโโโโโโโโ?โฏ**\n"
                    f"** โข  Sษชษขษดแดส   :** "
                    f"`%sms` \n"
                    f"** โข  Uแดแดษชแดแด  :** "
                    f"`{uptime}` \n"
                    f"** โข  Oแดกษดแดส   :** `{ALIVE_NAME}` \n" 
                    f"** โข  สแดแด แด?แดส  :** `7.0` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("สแดแดกสส")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**แดแดsแดแดษชแดแดษด**\n**** : `%sms`\n**แดษช sแดแดษชแดษช** : `{uptime}๐`" % (duration))


@register(outgoing=True, pattern="^Speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...โจ`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "โง **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **โโโโโโโโโโโโโโโโโ**\n\n"
                   "โง **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "โง **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "โง **Signal:** "
                   f"`{result['ping']}` \n"
                   "โง **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "โง **BOT:** ๐ฅแดษชษดแด-แดsแดสสแดแด๐ฅ")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^Pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("PONG")
    await asyncio.sleep(1)
    await pong.edit("๐ฅ")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**Oแดกษดแดส : {ALIVE_NAME}**\n`%sms`" % (duration))


CMD_HELP.update({
    "ping": "๐พ๐ค๐ข๐ข๐๐ฃ๐: `Ping` | `Lping` | `Xping` | `.ping` | `Sping`\
         \nโณ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n๐พ๐ค๐ข๐ข๐๐ฃ๐: `Speed`\
         \nโณ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n๐พ๐ค๐ข๐ข๐๐ฃ๐: `Pong`\
         \nโณ : Sama Seperti Perintah Ping."})
