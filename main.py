import os
import google.generativeai as genai
from telegram.ext import Updater, MessageHandler, Filters

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def reply(update, context):
    msg = update.message.text
    try:
        res = model.generate_content(msg)
        update.message.reply_text(res.text)
    except Exception as e:
        update.message.reply_text(str(e))

updater = Updater(TELEGRAM_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
updater.idle()
