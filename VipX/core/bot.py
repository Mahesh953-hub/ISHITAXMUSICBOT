
import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class VipXBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"😛ѕταяτιиg γουя ϐοτ😜")
        super().__init__(
            "VipXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"╔═══❰ 𝙎𝙬𝙖𝙜𝙖𝙩 ❱═══❍⊱❁۪۪\n║\n║┣⪼🥀𝘽𝙤𝙩 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 🎉\n║\n║◈ {config.MUSIC_BOT_NAME}\n║\n║┣⪼🎈𝐈𝐃:- `{self.id}` \n║\n║┣⪼🎄@{self.username} \n║ \n║┣⪼💖𝘿𝙝𝙖𝙣𝙮𝙒𝙖𝙖𝙙 😍\n║\n╚══════════════❍⊱❁"
            )
            
        except:
            LOGGER(__name__).error(
                "ƴουƦ Ƀοτ ιѕиτ α∂∂є∂ ιи ᏞοggєƦ ᏀᎡϴႮᏢ"
            )
            
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("start", "❥ ✨ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ✨"),
                        BotCommand("ping", "❥ 🍁ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ🍁"),
                        BotCommand("help", "❥ 🥺ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ🥺"),
                        BotCommand("vctag", "❥ 😇ᴛᴀɢᴀʟʟ ғᴏʀ ᴠᴄ🙈"),
                        BotCommand("stopvctag", "❥ 📍sᴛᴏᴘ ᴛᴀɢᴀʟʟ ғᴏʀ ᴠᴄ 💢"),
                        BotCommand("tagall", "❥ 🔻ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ʙʏ ᴛᴇxᴛ🔻"),
                        BotCommand("cancel", "❥ 🔻ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴛᴀɢɢɪɴɢ🔻"),
                        BotCommand("settings", "❥ 🔻ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴇᴛᴛɪɴɢs🔻"),
                        BotCommand("reload", "❥ 🪐ᴛᴏ ʀᴇʟᴏᴀᴅ ᴛʜᴇ ʙᴏᴛ🪐"),
                        BotCommand("play", "❥ ❣️ᴛᴏ ᴘʟᴀʏ ᴛʜᴇ sᴏɴɢ❣️"),
                        BotCommand("vplay", "❥ ❣️ᴛᴏ ᴘʟᴀʏ ᴛʜᴇ ᴍᴜsɪᴄ ᴡɪᴛʜ ᴠɪᴅᴇᴏ❣️"),
                        BotCommand("pause", "❥ 🥀ᴛᴏ ᴘᴀᴜsᴇ ᴛʜᴇ sᴏɴɢs🥀"),
                        BotCommand("resume", "❥ 💖ᴛᴏ ʀᴇsᴜᴍᴇ ᴛʜᴇ sᴏɴɢ💖"),
                        BotCommand("end", "❥ 🐚ᴛᴏ ᴇᴍᴘᴛʏ ᴛʜᴇ ϙᴜᴇᴜᴇ🐚"),
                        BotCommand("queue", "❥ 🤨ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ϙᴜᴇᴜᴇ🤨"),
                        BotCommand("playlist", "❥ 🕺ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴘʟᴀʏʟɪsᴛ🕺"),
                        BotCommand("stop", "❥ ❤‍🔥ᴛᴏ sᴛᴏᴘ ᴛʜᴇ sᴏɴɢs❤‍🔥"),
                        BotCommand("lyrics", "❥ 🕊️ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟʏʀɪᴄs🕊️"),
                        BotCommand("song", "❥ 🔸ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ sᴏɴɢ🔸"),
                        BotCommand("video", "❥ 🔸ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ᴠɪᴅᴇᴏ sᴏɴɢ🔸"),
                        BotCommand("gali", "❥ 🔻ᴛᴏ ʀᴇᴘʟʏ ғᴏʀ ғᴜɴ🔻"),
                        BotCommand("shayri", "❥ 🔻ᴛᴏ ɢᴇᴛ ᴀ sʜᴀʏᴀʀɪ🔻"),
                        BotCommand("love", "❥ 🔻ᴛᴏ ɢᴇᴛ ᴀ ʟᴏᴠᴇ sʜᴀʏᴀʀɪ🔻"),
                        BotCommand("sudolist", "❥ 🌱ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ sᴜᴅᴏʟɪsᴛ🌱"),
                        BotCommand("owner", "❥ 💝ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴏᴡɴᴇʀ💝"),
                        BotCommand("update", "❥ 🐲ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʙᴏᴛ🐲"),
                        BotCommand("gstats", "❥ 💘ᴛᴏ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ💘"),
                        BotCommand("repo", "❥ 🍌ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ 𝚁𝙴𝙿𝙾🍌")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Bᴏᴛ Isɴᴛ Aᴅᴍɪɴ Iɴ Yᴏᴜʀ Lᴏɢɢᴇʀ Gʀᴏᴜᴘ, Pʟᴇᴀsᴇ Mᴀᴋᴇ {config.MUSIC_BOT_NAME} Aᴅᴍɪɴ Tᴏ Wᴏʀᴋ"
            )
            
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"🎉Yᴏᴜʀ Mᴜsɪᴄ Bᴏᴛ Hᴀs Bᴇᴇɴ Sᴛᴀʀᴛᴇᴅ  \n🥀Nᴀᴍᴇ:- {self.name}")
