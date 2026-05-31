#8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34
from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    filters,
    MessageHandler,
    CommandHandler
)

TOKEN = "8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34"


keyboard = [
     [
          KeyboardButton("راهنما"),
          KeyboardButton("درباره ما")
     ]
]

markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start (update: Update ,context: ContextTypes.DEFAULT_TYPE ) :
    await update.message.reply_text(
         "سلام به ربات من خوش آمدی",
         reply_markup = markup
                                    )

async def help_command (update: Update ,context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text("""
    دستورات:
    /start
    /help
    """)

async def menu_handler (update: Update ,context: ContextTypes.DEFAULT_TYPE) :
       text = update.message.text
       if text == "راهنما" :
            await update.message.reply_text("""
                دستورات:
                /start
                /help
            """)

       elif text == "درباره ما" :
            await update.message.reply_text("این ربات برای آموزش ساخته شده است.")

       else :
            await update.message.reply_text(f"توگفتی: {text}")
        




app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CommandHandler("help",help_command )
)

app.add_handler(
     MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler)
)
print("ربات روشن شد...")

app.run_polling()