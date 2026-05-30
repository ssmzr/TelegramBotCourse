#8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34"

async def tekrar (update : Update ,context : ContextTypes.DEFAULT_TYPE ) :
    text = update.message.text
    await update.message.reply_text(f"tekrar: {text}")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT ,tekrar)
)

print("ربات روشن شد...")

app.run_polling()