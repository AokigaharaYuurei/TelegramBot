import telebot;
bot = telebot.TeleBot('8373075661:AAGcWEdBagAFDtgc_-vNwF7JdOo8V4lh_j4');

@bot.message_handler(content_type=['text'])
def get_text_messages(message):