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
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn', 
#         'password': 'python'
#     }
# }


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
    

def wordplanet(update, context):
    print('планета')
    user_text = update.message.text
    print (user_text)
    if context.args:
         user_text = 'mars'
         print('марс_атакаует')
         mars = ephem.Mars('2000/01/01')
         constellation = ephem.constellation(mars)
         update.message.reply_text(constellation[-1])
         print(constellation)
    else:
         update.message.reply_text("увы")

    

def main():
    mybot = Updater("уник",use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet",wordplanet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
