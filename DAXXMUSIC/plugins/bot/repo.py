from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ʜᴇʀᴇ ɪs ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ✪
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("sᴏᴜʀᴄᴇ", url=f"https://github.com/Sidhusaab0001/ShizuMusic")
        ],
               [
                InlineKeyboardButton("ᴏᴡɴᴇʀ", url="t.me/X_SIDHU"),

],
]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/d858b66dde84a24dc08cf.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------

