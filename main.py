import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

ADMIN_CHAT_ID = 1033014201  # رقم حسابك في التليجرام

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton('📩 SMS'),
        KeyboardButton('👥 جهات الاتصال'),
        KeyboardButton('📞 سجل المكالمات')
    )
    bot.send_message(message.chat.id, "أهلاً وسهلاً، اختر نوع الخدمة المطلوبة:", reply_markup=markup)

@bot.message_handler(func=lambda msg: True)
def handle_message(msg):
    text = msg.text
    user = msg.from_user
    name = user.first_name or "بدون اسم"
    username = f"@{user.username}" if user.username else "بدون يوزر"
    user_id = user.id

    if text == '📩 SMS':
        bot.send_message(msg.chat.id, "جاري إرسال ملف SMS 📄...")
        with open("sms.html", "rb") as f:
            bot.send_document(msg.chat.id, f, caption="ملف SMS المطلوب")
        bot.send_message(ADMIN_CHAT_ID, f"طلب من {name} ({username}) - ID: {user_id}\nالخدمة: SMS")

    elif text == '👥 جهات الاتصال':
        bot.send_message(msg.chat.id, "جاري إرسال ملف جهات الاتصال 📄...")
        with open("contacts.html", "rb") as f:
            bot.send_document(msg.chat.id, f, caption="ملف جهات الاتصال")
        bot.send_message(ADMIN_CHAT_ID, f"طلب من {name} ({username}) - ID: {user_id}\nالخدمة: جهات الاتصال")

    elif text == '📞 سجل المكالمات':
        bot.send_message(msg.chat.id, "جاري إرسال ملف سجل المكالمات 📄...")
        with open("calls.html", "rb") as f:
            bot.send_document(msg.chat.id, f, caption="ملف سجل المكالمات")
        bot.send_message(ADMIN_CHAT_ID, f"طلب من {name} ({username}) - ID: {user_id}\nالخدمة: سجل المكالمات")

    else:
        bot.send_message(msg.chat.id, "اختر من الأزرار فقط 🙏")
        bot.send_message(ADMIN_CHAT_ID, f"رسالة من {name} ({username}) - ID: {user_id}\nالنص: {text}")

bot.infinity_polling()
