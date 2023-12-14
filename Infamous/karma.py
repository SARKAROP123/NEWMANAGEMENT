# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/40b93b46642124605e678.jpg",
    "https://telegra.ph/file/01a2e0cd1b9d03808c546.jpg",
    "https://telegra.ph/file/ed4385c26dcf6de70543f.jpg",
    "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg",
    "https://telegra.ph/file/cce9038f6a9b88eb409b5.jpg",
    "https://telegra.ph/file/262c86393730a609cdade.jpg",
    "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg",
]

HEY_IMG = "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

BAN_GIFS = [
    "https://telegra.ph//file/85ac1ab12c833afa1a5dd.mp4",
]


KICK_GIFS = [
    "https://telegra.ph//file/79a6c527e6e6d530bcdc8.mp4",
]


MUTE_GIFS = [
    "https://telegra.ph//file/b4faf6e390d72d286abdf.mp4",
]

FIRST_PART_TEXT = "🍷 *𝗛𝗘𝗬 `{}` . . . 𝗜 𝗔𝗠 𝗠𝗨𝗦𝗜𝗖 𝗔𝗡𝗗 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧 𝗕𝗢𝗧✨*"

PM_START_TEXT = "*💥𝗜 𝗔𝗠 ✭𝗔𝗗𝗩𝗔𝗡𝗖𝗘 ✭𝗔𝗡𝗗✭ 𝗦𝗨𝗣𝗘𝗥𝗙𝗔𝗦𝗧 ✭𝐌υѕι¢ ✭𝐁σт 𝐈и 𝐓єℓєgяαм ✭𝐆яσυρ🎸  + /mstart 𝗠𝗨𝗦𝗜𝗖 𝗖𝗠𝗡𝗗 + /help 𝐆𝐢𝐯𝐞 𝐘𝐨𝐮 𝐓𝐡𝐢𝐬 𝐌𝐞𝐬𝐬𝐚𝐠𝐞.💥𝐈 αм ✭𝐀∂ναи¢є ✭𝐌єииαgє✭ 𝐘συя ✭𝐒υρєя ✭𝐆яσυρ✭ 💞 *"

START_BTN = [
    [
        InlineKeyboardButton(
            text="➕𝗔𝗗𝗗 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="✫𝗛𝗘𝗟𝗣✫", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="✫𝗕𝗢𝗧 𝗜𝗡𝗙𝗢✫", callback_data="Miko_"),
        InlineKeyboardButton(text="𝗔𝗟𝗟", callback_data="ai_handler"),
    ],
    [
        InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="➕𝗔𝗗𝗗 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="𝗢𝗪𝗡𝗘𝗥", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="𝗨𝗣𝗗𝗔𝗧𝗘", url="https://t.me/TKS_JOIN"),
        ib(text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/TKS_CHAT_OFFICIAL"),
    ],
    [
        ib(
            text="➕𝗔𝗗𝗗 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *𝗜 𝗔𝗠 𝗬𝗢𝗨𝗥 𝗛𝗘𝗟𝗣𝗜𝗡𝗚* 🫧

☉ *𝗜 𝗔𝗠 𝗙𝗨𝗟𝗟 𝗛𝗘𝗟𝗣𝗜𝗡𝗚 𝗬𝗢𝗨 𝗠𝗨𝗦𝗜𝗖 𝗔𝗡𝗗 𝗠𝗔𝗡𝗔𝗚𝗘𝗜𝗡𝗚 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣.*

𝗔𝗟𝗟 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗖𝗔𝗡 𝗕𝗘 𝗨𝗦𝗘𝗗 𝗪𝗜𝗧𝗛 : /
"""
