"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planet_of_sun_system(update, context):
    today = date.today().strftime('%Y/%m/%d')
    user_text = update.message.text.split()
    name_of_planet = user_text[1]
    planets = {
            'Mercury': ephem.Mercury,
            'Venus': ephem.Venus,
            'Mars': ephem.Mars,
            'Jupiter': ephem.Jupiter,
            'Saturn': ephem.Saturn,
            'Uranus': ephem.Uranus,
            'Neptune': ephem.Neptune
        }
    if name_of_planet in planets:
        const = ephem.constellation(planets[name_of_planet](today))
        print(*const)
        update.message.reply_text(const)



def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def main():
    mybot = Updater("8844848511:AAH9jQNge0m00n1uGnV3F9ZjTfToR5haXXE", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_of_sun_system))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
