import telebot
from telebot import types
import sqlite_client

bot = telebot.TeleBot("7110938286:AAGASN2rHpmujt08R1sTGWPuequDext7DLc", parse_mode='HTML')

def send_all(msg_pattern):
    clients = sqlite_client.get_all_clients()
    counter = 0
    for client in clients:
        bot.send_message(client[0], f'{client[1] + "," if client[1] is not None else ""}{msg_pattern}')
        counter += 1
        print(f'progress: {counter} / {len(clients)}')

send_all('privet, y nas super akciya')