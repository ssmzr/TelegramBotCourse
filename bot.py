#8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    filters,
    MessageHandler,
    CommandHandler
)

TOKEN = "8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34"

async def start (update: Update ,context: ContextTypes.DEFAULT_TYPE ) :
    await update.message.reply_text("سلام به ربات من خوش آمدی")

async def help_command (update: Update ,context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text("""
    دستورات:
    /start
    /help
    """)

async def echo (update: Update ,context: ContextTypes.DEFAULT_TYPE) :
       text = update.message.text
       await update.message.reply_text(f"تو گفتی : {text}")



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CommandHandler("help",help_command )
)

app.add_handler(
     MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
)
print("ربات روشن شد...")

app.run_polling()