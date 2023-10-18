from VipX import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

TEXT = [ "**Oʏᴇ, Vᴄ Jᴏɪɴ Kʀʟᴏ Nᴀ 🥲**",
         "**Vᴄ Jᴏɪɴ Kʀʟᴏ Jᴀʟᴅɪ😬**",
         "**Cᴏᴍᴇ Vᴄ 🏓**",
         "**Bᴀʙᴜ, Vᴄ Aᴀᴏɴᴀ Eᴋ Bᴀᴀʀ 🥰**",
         "**Oʏᴇ, Vᴄ Aᴀ Eᴋ Kᴀᴀᴍ ʜ🤨**",
         "**Sᴜɴᴏ Nᴀ 🥺, Vᴄ Jᴏɪɴ Kʀʟᴏ 🤣**",
         "**Vᴄ Aᴀᴊᴀɪʏᴇ Eᴋ Bᴀᴀʀ 😁**",
         "**Vᴄ Pᴇ Bᴅʜɪʏᴀ Sᴀ Gᴀᴍᴇ Cʜᴀʟ Rʜᴀ, Aᴊᴀᴏ Pʟᴀʏ Kʀᴇ⚽**",
         "**Cʜᴜᴘ Cʜᴀᴘ Vᴄ Jᴏɪɴ Kʀᴏ Vʀɴᴀ Bᴀᴍ Kʀʀ Dᴜɴɢɪ 😂**",
         "**Sᴏʀʀʏ Bᴇᴀʙs, Pʟᴇᴇᴅʜ Vᴄ Jᴏɪɴ Kʀʟᴏ Nᴀ 😥**",
         "**Vᴄ Aᴀᴠᴏ Eᴋ Bᴅʜɪʏᴀ Sɪɪ Cʜɪᴢ Dɪᴋʜᴀᴛɪ 🙄**",
         "** Vᴄ Cʜᴇᴄᴋ Kʀᴋᴇ Bᴛᴀɴᴀ Tᴏʜ Kᴏɴsᴀ Sᴏɴɢ Pʟᴀʏ Hᴏ Rʜᴀ 🤔**",
         "**Vᴄ Jᴏɪɴ Kʀʟᴏ Nᴀ Pʟᴇᴇᴅʜ 🥺**",
         "**Vᴄ Pᴇ Lᴀᴅᴀɪ Hᴏɢʏɪ, Aᴊᴀᴏ Jᴀʟᴅɪ **",
         "**Tᴜᴍsᴇ Bᴀᴀᴛ Kʀɴɪ Tʜɪ, Vᴄ Aᴊᴀᴏ 🥺💖**",
         "**Mᴇʀᴇ Sᴇ Kᴏɪ Bᴀᴀᴛ Nᴏɪɪ Kʀᴛᴀ, Tᴜᴍ Kʀʟᴏ Nᴀ Vᴄ Pᴇ 🥺**",
         "**Vᴄ Pᴇ Lᴀᴅᴀɪ Hᴏɢʏɪ Kʜᴀᴛᴀʀɴᴀᴀᴋ Wᴀʟɪ, Aᴊᴀᴏ Jᴀʟᴅɪ**",
         
        ]

@app.on_message(filters.command(["vctag", "vctagall"], prefixes=["/", ".", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == "private":
        return await message.reply("Tʜɪs Cᴏᴍᴍᴀɴᴅ Is Oɴʟʏ Fᴏʀ Gʀᴏᴜᴘs ❗❗.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("Yᴏᴜ Aʀᴇ Nᴏᴛ Aɴ Aᴅᴍɪɴ Tᴏ Pᴇʀғᴏʀᴍ Tʜɪs Aᴄᴛɪᴏɴ, Asᴋ Tᴏ Oᴡɴᴇʀ Tᴏ Mᴀᴋᴇ Yᴏᴜ Aᴅᴍɪɴ Aɴᴅ Tʀʏ Aɢᴀɪɴ. ")

    if message.reply_to_message and message.text:
        return await message.reply("/Vctag Vᴄ Aᴊᴀᴏ Sᴀʙ 💝💝 Oʀ Rᴇᴘʟʏ Tᴏ Msɢ.")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/Vctag Vᴄ Aᴊᴀᴏ Sᴀʙ 💝💝 Oʀ Rᴇᴘʟʏ Tᴏ Msɢ.")
    else:
        return await message.reply("/Vctag Vᴄ Aᴊᴀᴏ Sᴀʙ 💝💝 Oʀ Rᴇᴘʟʏ Tᴏ Msɢ.")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TEXT)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(TEXT)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancel", "stop", "stopvctag", "vctagstop", "cancelvctag", "canceltag", "stoptag", "stoptagall", "canceltagall"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("I Aᴍ Nᴏᴛ Tᴀɢɢɪɴɢ 😴.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in ("administrator", "creator"):
            is_admin = True
    if not is_admin:
        return await message.reply("Yᴏᴜ Aʀᴇ Nᴏᴛ Aɴ Aᴅᴍɪɴ Tᴏ Pᴇʀғᴏʀᴍ Tʜɪs Aᴄᴛɪᴏɴ, Asᴋ Tᴏ Oᴡɴᴇʀ Tᴏ Mᴀᴋᴇ Yᴏᴜ Aᴅᴍɪɴ Aɴᴅ Tʀʏ Aɢᴀɪɴ. ")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("Mᴇɴᴛɪᴏɴ Pʀᴏᴄᴇss Cᴇɴᴄᴇʟɪɴɢ 💔")
        

        

