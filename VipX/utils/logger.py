from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from VipX import app
from VipX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
┏━━━🔸 Pʟᴀʏɪɴɢ🔹━━━┓۪۪

◈ Cʜᴀᴛ ➪ **{message.chat.title}**

◈ Cʜᴀᴛ Iᴅ ➪ `{message.chat.id}`

◈ Usᴇʀ ➪ **{message.from_user.mention}**

◈ UsᴇʀNᴀᴍᴇ ➪ **@{message.from_user.username}**

◈ Iᴅ ➪ `{message.from_user.id}`

◈ Cʜᴀᴛ Nᴀᴍᴇ ➪ **{chatusername}**

◈ Sᴇᴀʀᴄʜᴇᴅ ➪ **{message.text}**

◈ Bʏ ➪ **{streamtype} ▄ █ ▄ █ ▄**

┗━━━🔸 #NᴇᴡSᴏɴɢ🔹━━━┛۪۪"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
