import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")

def calculator(update, context):
    text = update.message.text
    try:
        result = eval(text)
        update.message.reply_text(str(result))
    except:
        update.message.reply_text("❌ أرسل عملية حسابية مثل: 3+4")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calculator))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
