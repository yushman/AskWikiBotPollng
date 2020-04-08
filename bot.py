import logging

import telebot
import wiki_test

TOKEN = '1037297582:AAEZgpqDOWaHIyoX9CWJpn_aJ_hAZwGAVQw'

bot = telebot.TeleBot(TOKEN)
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.send_message(message.from_user.id, "Hi, type /help to help, type query to perform wiki search")


@bot.message_handler(commands=['help'])
def send_welcome_message(message):
    bot.send_message(message.from_user.id, "Hi, type query to perform wiki search")


@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    if message.content_type == "text":
        search_results = wiki_test.proceedSearch(message.text)
        if search_results is not None:
            for result in search_results:
                bot.send_message(message.from_user.id, result)
        else:
            bot.send_message(message.from_user.id, "Some error in wiki search, try to make another search")
    else:
        bot.send_message(message.from_user.id, "I don't understand you. type /help for help.")


bot.polling(True, 3)
