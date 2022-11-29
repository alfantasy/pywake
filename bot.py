import telebot # подключение библиотеки pyTelegramBotAPI
import logging # библиотека журнала
# для запуска скриптов
from subprocess import call
# настройки для журнала
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('telegramBot.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
# создание бота с его токеном API
bot = telebot.TeleBot("5605394784:AAE6v-vSaji4H9CIR-GNchhzrIn94xnHBQ0")
chat_id = "637816895"
# Разрешенный user-id
my_user_id = 637816895
# текст справки
help_string = []
help_string.append("Это мой домашний минибот.\n\n")
help_string.append("/start - выводит приветствие;\n")
help_string.append("/help - отображает эту справку;\n")
help_string.append("/stats - присылает статус девайса;\n")
help_string.append("/powerpc- включает домашний компьютер.")
# --- команды
@bot.message_handler(commands=['start']) #Отвечаем на команду /start
def send_start(message):
# отправка простого сообщения
    to_check_id = message.from_user.id #Получаем user-id пользователя, который обратился к нашему боту
    if to_check_id == to_check_id: #Проверяем, совпадает ли этот user-id с тем, которому мы доверяем
        response_message = to_check_id
    else:
        response_message = "Ты кто такой? Я тебя не знаю, уходи."
    bot.reply_to(message, response_message)

@bot.message_handler(commands=['help']) #Отвечаем на команду /help
def send_help(message):
    # отправка сообщения с поддержкой разметки Markdown
    to_check_id = message.from_user.id
    if to_check_id == my_user_id:
        bot.send_message(chat_id, "".join(help_string), parse_mode="Markdown")
    else:
        response_message = "Ты кто такой? Я тебя не знаю, уходи."
@bot.message_handler(commands=['stats']) #Отвечаем на команду /stats
def send_router(message):
    to_check_id = message.from_user.id
    if to_check_id == my_user_id:
        try:
# по этому пути лежит скрипт сбора информации по статусам девайса
# читает файл с результатами выполнения скрипта
            call(["/root/pywake/statustotelegram.sh"])
            status = open("/root/pywake/statustotelegram.txt", "rb").read()
            bot.send_message(chat_id, status, parse_mode="Markdown")
        except Exception as e:
            logger.exception(str(e))
            bot.send_message(chat_id, "Ошибка при получении статуса роутера. Подробности в журнале.")
        else:
            response_message = "Ты кто такой? Я тебя не знаю, уходи."
@bot.message_handler(commands=['powerpc']) # Отвечаем на команду /powerpc
def send_wakepc(message):
    to_check_id = message.from_user.id
    if to_check_id == my_user_id:
        try:
    # тут скрипт включения компа
            call(["/root/pywake/powerpc.sh"])
    # пишем что команда выполнена
            bot.send_message(chat_id, "Команда выполнена!")
        except Exception as e:
            logger.exception(str(e))
            bot.send_message(chat_id, "Ошибка при выполнении скрипта. Подробности в журнале.")
        else:
            response_message = "Ты кто такой? Я тебя не знаю, уходи."
# запуск приёма сообщений
bot.polling()
