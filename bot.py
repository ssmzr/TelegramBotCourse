from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من اولین ربات تو هستم 😎")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("ربات روشن شد...")

app.run_polling()