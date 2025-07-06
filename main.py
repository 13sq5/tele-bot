import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('📩 SMS'), KeyboardButton('👥 جهات الاتصال'), KeyboardButton('📞 سجل المكالمات'))
    bot.send_message(message.chat.id, "أهلاً وسهلاً، اختر نوع الخدمة المطلوبة:", reply_markup=markup)

@bot.message_handler(func=lambda msg: True)
def handle_message(msg):
    text = msg.text
    if text == '📩 SMS':
        bot.send_message(msg.chat.id, "تم استلام طلب SMS ✅")
    elif text == '👥 جهات الاتصال':
        bot.send_message(msg.chat.id, "تم استلام طلب جهات الاتصال ✅")
    elif text == '📞 سجل المكالمات':
        bot.send_message(msg.chat.id, "تم استلام طلب سجل المكالمات ✅")
    else:
        bot.send_message(msg.chat.id, "اختر من الأزرار فقط 🙏")

bot.infinity_polling()
