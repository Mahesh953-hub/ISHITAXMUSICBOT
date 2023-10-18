from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
# Command
PLAY_COMMAND = get_command("PLAY_COMMAND")
GSTATS_COMMAND =get_command("GSTATS_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
REBOOT_COMMAND = get_command("REBOOT_COMMAND")
STOP_COMMAND = get_command("STOP_COMMAND")
SKIP_COMMAND = get_command("SKIP_COMMAND")
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")
SEEK_COMMAND = get_command("SEEK_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
UNGBAN_COMMAND = get_command("UNGBAN_COMMAND")
GBANNED_COMMAND = get_command("GBANNED_COMMAND")
SETTINGS_COMMAND = get_command("SETTINGS_COMMAND")
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
GETVAR_COMMAND = get_command("GETVAR_COMMAND")
UPDATE_COMMAND = get_command("UPDATE_COMMAND")
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")
ADDSUDO_COMMAND = get_command("ADDSUDO_COMMAND")
DELSUDO_COMMAND = get_command("DELSUDO_COMMAND")
GETLOG_COMMAND = get_command("GETLOG_COMMAND")
BROADCAST_COMMAND = get_command("BROADCAST_COMMAND")
AUTH_COMMAND = get_command("AUTH_COMMAND")
UNAUTH_COMMAND = get_command("UNAUTH_COMMAND")
BLACKLISTCHAT_COMMAND = get_command("BLACKLISTCHAT_COMMAND")
UNBLOCK_COMMAND = get_command("UNBLOCK_COMMAND")
BLOCK_COMMAND = get_command("BLOCK_COMMAND")
GBAN_COMMAND = get_command("GBAN_COMMAND")

@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2ff2dab0dd5953e674c79.jpg",
        caption=f"""Cʟɪᴄᴋ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tᴏ Cᴏɴᴛᴀᴄᴛ Mʏ Oᴡɴᴇʀ 😙""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aɴᴅʀᴏɪᴅ Usᴇʀ", url=f"https://t.me/AnDrOiiiDUsEr")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GBANNED_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GBANNED_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2ff2dab0dd5953e674c79.jpg",
        caption=f"""Cʟɪᴄᴋ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tᴏ Cᴏɴᴛᴀᴄᴛ Mʏ Oᴡɴᴇʀ 😙""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aɴᴅʀᴏɪᴅ Usᴇʀ", url=f"https://t.me/AnDrOiiiDUsEr")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""Cʟɪᴄᴋ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tᴏ Gᴇᴛ Rᴇᴘᴏ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""Cʟɪᴄᴋ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tᴏ Gᴇᴛ Rᴇᴘᴏ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""Cʟɪᴄᴋ Tʜᴇ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ Tᴏ Gᴇᴛ Rᴇᴘᴏ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

#Must Learn 

@app.on_message(
    filters.command(PLAY_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /play .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GSTATS_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /gstats .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /pause .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(REBOOT_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /reboot .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /stop .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SKIP_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /skip .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ACTIVEVIDEO_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )



@app.on_message(
    filters.command(ACTIVEVC_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ACTIVEVC_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ACTIVEVIDEO_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command(GETVAR_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GETVAR_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command(SEEK_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /seek (count) .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(RESUME_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /resume .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(SETTINGS_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /settings .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(GBAN_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command(GBAN_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNGBAN_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNGBAN_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(RELOAD_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /reload .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UPDATE_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UPDATE_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SPEEDTEST_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SPEEDTEST_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ADDSUDO_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Mʏ Oᴡɴᴇʀ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ADDSUDO_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Mʏ Oᴡɴᴇʀ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(DELSUDO_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Mʏ Oᴡɴᴇʀ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(DELSUDO_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Mʏ Oᴡɴᴇʀ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BROADCAST_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BROADCAST_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(AUTH_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /auth .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNAUTH_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs, Aᴅᴅ ᴍᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ Aɴᴅ Usᴇ /unauth .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BLACKLISTCHAT_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BLACKLISTCHAT_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(BLOCK_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BLOCK_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNBLOCK_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNBLOCK_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Sᴜᴅᴏ Usᴇʀs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Mᴇ Bᴇᴀʙs 😙💝", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

