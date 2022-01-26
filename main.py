from pyrogram import Client, filters

Naruto=Client(
    "Imdb Bot",
    bot_token="5156565463:AAHUNBZIQygwcNVeBr0NZPlyP_rWnMCGQt4",
    api_id="15316155",
    api_hash="c2340e29da60393bc3c96fa7c0870911"
)
@Naruto.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("Hey Bro Eth Give Way Gruop Anu ketto😅")

@Naruto.on_message(filters.command("help"))
async def start_message(bot, message):
    await message.reply_text("ദെയിവമേ എന്ന മാത്രം രക്ഷികനെ😅")





Naruto.run()
