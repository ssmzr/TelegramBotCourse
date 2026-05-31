#8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler
)

TOKEN = "8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34"

async def start (update : Update ,context : ContextTypes.DEFAULT_TYPE ) :
    await update.message.reply_text("سلام به ربات من خوش آمدی")

async def help (update : Update ,context : ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text("""
    دستورات:
    /start
    /help
    """)



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CommandHandler("help",help )
)
print("ربات روشن شد...")

app.run_polling()