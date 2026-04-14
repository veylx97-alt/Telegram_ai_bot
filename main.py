import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    try:
        res = model.generate_content(msg)
        await update.message.reply_text(res.text)
    except Exception as e:
        await update.message.reply_text(str(e))

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

app.run_polling()
import sys
print(sys.version)
print(sys.modules.keys())
