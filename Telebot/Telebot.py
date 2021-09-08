# -*- coding: utf-8 -*-

import telebot
from aiogram import types

print("Бот запущен")
bot = telebot.TeleBot('1950193798:AAFZzhg2IsF1i0ZKTpm02AeVaHtYGQuYUy8')


@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, "К сожелению игра еще не доступна")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет " + message.from_user.first_name + "!")
    else:
        bot.send_message(message.from_user.id, "Введите команду /start")


bot.polling(none_stop=True, interval=0)


