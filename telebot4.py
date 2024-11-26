import telebot
from telebot import types
import sqlite_client

bot = telebot.TeleBot("7110938286:AAGASN2rHpmujt08R1sTGWPuequDext7DLc", parse_mode='HTML')



@bot.message_handler(commands=['start'])
def run(message):
    keyboard = types.ReplyKeyboardMarkup()
    button_phone = types.KeyboardButton(text="otpravitb nomer", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, f'spasibo mi s vami svyazhemsya', reply_markup=keyboard)



@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    name = message.contact.first_name
    phone = message.contact.phone_number
    tg_id = message.from_user.id
    username = message.from_user.username
    sqlite_client.save_phone_to_db(tg_id, phone, name, username)

bot.infinity_polling()
