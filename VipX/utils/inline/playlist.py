from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Pᴇʀsᴏɴᴀʟ 💝",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="Gʟᴏʙᴀʟ 💞", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Cʟᴏsᴇ 🔪", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Tᴏᴘ 10 Lɪsᴛ ❤️", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="Oᴡɴ 💖", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="Gʟᴏʙᴀʟ 💞", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="Gʀᴏᴜᴘ 💕", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="Bᴀᴄᴋ 💓", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="Cʟᴏsᴇ 🔪", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴜᴅɪᴏ 🎧", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="Vɪᴅᴇᴏ 🎬", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bᴀᴄᴋ 💕", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="Cʟᴏsᴇ 🔪", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Tᴏᴘ 10 Lɪsᴛ ❤️", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="Pᴇʀsᴏɴᴀʟ 💝", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="Gʟᴏʙᴀʟ 💞", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="Gʀᴏᴜᴘ 💕", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="Bᴀᴄᴋ 💕", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="Cʟᴏsᴇ 🔪", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Bᴀᴄᴋ 💕",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="Cʟᴏsᴇ 🔪", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Dᴇʟᴇᴛᴇ 🔪🔪",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Bᴀᴄᴋ 💕",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="Cʟᴏsᴇ 🔪",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Cʟᴏsᴇ 🔪",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
