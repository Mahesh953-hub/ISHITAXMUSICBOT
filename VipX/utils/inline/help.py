from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
        InlineKeyboardButton(
            text="Mᴏʀᴇ 💞", callback_data="help_callback hb13"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Aᴅᴍɪɴ ❤️",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Aᴜᴛʜ 🧡",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="Bʟᴏᴄᴋ 💔",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Gᴄᴀsᴛ 💞",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="Gʙᴀɴ 💔",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="Lʏʀɪᴄs 💗",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="PʟᴀʏLɪsᴛ 💝",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="Vᴏɪᴄᴇ Cʜᴀᴛ 💘",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="Pʟᴀʏ 💖",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="Sᴜᴅᴏ 💚",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Sᴛᴀʀᴛ ❤️",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="Mᴏʀᴇ 💓", callback_data="help_callback hb13"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Hᴇʟᴘ 💞",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons


