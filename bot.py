
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from telegram.ext import (
    filters,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    CommandHandler,
    ApplicationBuilder,
    CallbackQueryHandler
     )

TOKEN = "8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34"

keyboard = [
    [InlineKeyboardButton("راهنما", callback_data="help")],
    [InlineKeyboardButton("درباره ما", callback_data="about")]
]

markup = InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام به ربات من خوش اومدی", reply_markup=markup)
    
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "help" :
        await query.message.reply_text("""
        دستورات:
        /start
        /help
        /about

        """)
    elif query.data == "about":
         await query.message.reply_text("این یک ربات آموزشی است")







app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)


app.add_handler(
    CallbackQueryHandler(button_handler)
)




print("ربات روشن شد...")
app.run_polling()






