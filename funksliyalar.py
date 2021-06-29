# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:57:34 2021

@author: WINDOWS 10
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '1820835766:AAE03N4f5FHrzgp3zs0V_o7VXVMIXSdUd0o'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz! "
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg )if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()



