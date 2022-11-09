from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup


button1 = InlineKeyboardButton(text="👍",callback_data="like")
button2 = InlineKeyboardButton(text="👎",callback_data="dislike")

keyboard = InlineKeyboardMarkup().row(button1,button2)

button3 = InlineKeyboardButton(text="String",callback_data="string")
button4 = InlineKeyboardButton(text="For",callback_data="for")
button5 = InlineKeyboardButton(text="Dictionaries",callback_data="dct")
button6 = InlineKeyboardButton(text="Def",callback_data="def")
keyboard1 = InlineKeyboardMarkup(row_width=2).add(button3,button4,button5,button6)
