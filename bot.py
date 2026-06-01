#8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34
from telegram import Update

from telegram.ext import (
    filters,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    CommandHandler,
    ApplicationBuilder
     )

TOKEN = "8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34"

NAME, AGE, CITY = range(3)


async def start (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اسمت چیه ؟")

    return NAME

async def get_name (update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("چند سالته؟ ")

    return AGE

async def get_age (update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    context.user_data["age"] = update.message.text
    await update.message.reply_text("شهرت چیه؟ ")

    return CITY

async def get_city (update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["city"] = update.message.text
    await update.message.reply_text(
    f"""
✅ ثبت نام با موفقیت انجام شد

👤 نام: {context.user_data["name"]}
🎂 سن: {context.user_data["age"]}
🏙 شهر: {context.user_data["city"]}
"""
)

    return ConversationHandler.END

app = ApplicationBuilder().token(TOKEN).build()

conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start)
    ],

    states = {
        NAME:[
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)
        ],

        AGE: [
            MessageHandler(filters.Text & ~filters.COMMAND, get_age)

        ],
        
        CITY: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_city)

        ]

    },

    fallbacks= []
)

app.add_handler(conv_handler)
print("ربات روشن شد...")
app.run_polling()






