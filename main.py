import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

ADMIN_CHAT_ID = 1033014201  # هذا رقم شاتك الخاص

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
        bot.send_message(ADMIN_CHAT_ID, f"عميل @{msg.from_user.username} طلب خدمة SMS")
    elif text == '👥 جهات الاتصال':
        bot.send_message(msg.chat.id, "تم استلام طلب جهات الاتصال ✅")
        bot.send_message(ADMIN_CHAT_ID, f"عميل @{msg.from_user.username} طلب خدمة جهات الاتصال")
    elif text == '📞 سجل المكالمات':
        bot.send_message(msg.chat.id, "تم استلام طلب سجل المكالمات ✅")
        bot.send_message(ADMIN_CHAT_ID, f"عميل @{msg.from_user.username} طلب خدمة سجل المكالمات")
    else:
        bot.send_message(msg.chat.id, "اختر من الأزرار فقط 🙏")
        bot.send_message(ADMIN_CHAT_ID, f"رسالة من @{msg.from_user.username}: {text}")

bot.infinity_polling()
