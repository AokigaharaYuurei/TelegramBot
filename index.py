import telebot

# Ошибка 1: Telebot с маленькой буквы (должно быть с большой)
bot = telebot.TeleBot('8373075661:AAGcWEdBagAFDtgc_-vNwF7JdOo8V4lh_j4')

# Ошибка 2: massage_landler вместо message_handler
# Ошибка 3: content_types вместо content_types
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)