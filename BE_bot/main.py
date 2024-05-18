import telebot
from fgf import *
from time import sleep


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Столица Германии?":
        bot.send_message(message.from_user.id, 'Берлин')
        sleep(3)
    elif message.text == "Столица России?":
        bot.send_message(message.from_user.id, 'Москва')
        sleep(3)
    elif message.text == "Столица Японии?":
        bot.send_message(message.from_user.id, 'Токио')
        sleep(2)
    elif message.text == "Столица Франции?":
        bot.send_message(message.from_user.id, 'Париж')
        sleep(3)
    elif message.text == "Столица США?":
        bot.send_message(message.from_user.id, 'Вашингтон')
        sleep(3)
    elif message.text == "Столица Турции?":
        bot.send_message(message.from_user.id, 'Анкара')
        sleep(3)
    elif message.text == "Столица Египета?":
        bot.send_message(message.from_user.id, 'Каир')
        sleep(3)
    elif message.text == "Столица Бразилии?":
        bot.send_message(message.from_user.id, 'Бразилиа')
        sleep(3)
    elif message.text == "Столица Китая?":
        bot.send_message(message.from_user.id, 'Пекин')
        sleep(3)
    elif message.text == "Столица Италии?":
        bot.send_message(message.from_user.id, 'Рим')
        sleep(3)
    elif message.text == "Столица Испании?":
        bot.send_message(message.from_user.id, 'Мадрид')
        sleep(3)
    elif message.text == "Столица Канада?":
        bot.send_message(message.from_user.id, 'Оттава')
        sleep(3)
    elif message.text == "Столица Австралии?":
        bot.send_message(message.from_user.id, 'Канберра')
        sleep(3)
    elif message.text == "Столица Кыргызстана?":
        bot.send_message(message.from_user.id, 'Бишкек')
        sleep(3)
    elif message.text == "Столица Великобритании?":
        bot.send_message(message.from_user.id, 'Лондон')
        sleep(3)
    elif message.text == "Столица Индии?":
        bot.send_message(message.from_user.id, 'Дели')
        sleep(3)
    elif message.text == "Столица Таиланда?":
        bot.send_message(message.from_user.id, 'Бангкок')
        sleep(3)
    elif message.text == "Столица Мексики?":
        bot.send_message(message.from_user.id, 'Мехико')
        sleep(3)
    elif message.text == "Столица Швеции?":
        bot.send_message(message.from_user.id, 'Стокгольм')
        sleep(2)
    elif message.text == "Столица Сирии?":
        bot.send_message(message.from_user.id, 'Дамаск')
        sleep(2)
    elif message.text == "Столица Ирака?":
        bot.send_message(message.from_user.id, 'Багдад')
        sleep(2)
    elif message.text == "Столица Ирана?":
        bot.send_message(message.from_user.id, 'Тегеран')
        sleep(2)
    elif message.text == "Столица Вьетнама?":
        bot.send_message(message.from_user.id, 'Ханой')
        sleep(2)
    elif message.text == "Столица Пакистана?":
        bot.send_message(message.from_user.id, 'Исламбад')
        sleep(2)
bot.infinity_polling()


