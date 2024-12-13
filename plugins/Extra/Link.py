from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("link"))
async def generate_link(client, message):
    command_text = message.text.split(maxsplit=1)
    if len(command_text) < 2:
        await message.reply("**Please provide the name for the movie!\nExample :-** `/link Red One`")
        return
    movie_name = command_text[1].replace(" ", "-")
    link = f"https://telegram.me/Star_Moviess_Bot?start=getfile-{movie_name}"
    
    await message.reply(
        text=f"**Here is your Link :- [{movie_name}]({link})**",  # Bold movie name with regular font
        parse_mode=enums.ParseMode.MARKDOWN,  # Using Markdown formatting
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url={link}")]]
        )
    )
