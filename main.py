from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Naruto=Client(
    "Imdb Bot",
    bot_token="5156565463:AAHUNBZIQygwcNVeBr0NZPlyP_rWnMCGQt4",
    api_id="15316155",
    api_hash="c2340e29da60393bc3c96fa7c0870911"
)

@Naruto.on_message(filters.command("start"))
async def start_message(bot, message):
   await message.reply_text(
       text="JOIN",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("JOIN GRUOP", url="t.me/nanmapookal")
          ]]
          )
       )
   

Naruto.run()
