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
       text="**ഈ ചാനലിലും ഗ്രുഒപ്പിലും നിങ്ങൾ ഇല്ല ഇത്രെയും വേഗം ജോയിൻ ആവേണ്ടതാണ്🔥🔥**",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("🌹JOIN GRUOP🌹", url="t.me/midnightmoviesofficial"),
          InlineKeyboardButton ("🌹JOIN CHANNEL🌹", url="t.me/FILE_ADD_CHANNEL")
          ],[
          InlineKeyboardButton ("🌹BOT OWNER🌹", url="t.me/TEAM_NARUTO_GRUOP")
          InlineKeyboardButton ("🌹BOT DEV🌹", url="t.me/PR0FESS0R_99")
          InlineKeyboardButton ("🌹BOT EDITING🌹", url="t.me/TEAM_NARUTO_GRUOP")
          InlineKeyboardButton ("🌹REPO MAKE PART 1🌹", url="https://youtu.be/Af055Eozk9s")
          InlineKeyboardButton ("🌹SOURCE CODE🌹", url="https://github.com/SPIDEY-USER/IMDBFILTER")
          ]]
          )
       )
   

Naruto.run()
