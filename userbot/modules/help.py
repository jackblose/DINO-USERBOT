# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**`PERASAAN INI TIDAK DITEMUKAN,INGAT KATA KASIR ALFAMART!`**")
            await asyncio.sleep(100)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t π¦  "
        await event.edit("**π₯α΄ΙͺΙ΄α΄-α΄sα΄ΚΚα΄α΄π₯**\n\n"
                         f"**πΉ πΏπ΄πΌπΈπ»πΈπΊ π±πΎπ : {DEFAULTUSER}**\n**πΉ  πΌπΎπ³ππ»π΄π : {len(modules)}**\n\n"
                         "**πΉ ππ΄πΌππ° πΌπ΄π½π :**\n\n ββββββββββββββ£β β ββ βββββββββββββ\n\n"
                         f"πΉ {string}\n\n ββββββββββββββ£β β ββ βββββββββββββ\n\nNGETIK YANG BENER YA BUDUH!!\n\n")
        await event.reply(f"\n**Contoh** : Ketik <`.help ping`> Untuk Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba wahahaha..")
        await asyncio.sleep(50)
        await event.delete()
