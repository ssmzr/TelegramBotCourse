#8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34
from telegram import Update


from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    filters,
    MessageHandler,
    CommandHandler,
    ConversationHandler
)

TOKEN = "8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34"
NAME, AGE = range(2)

async def start (update: Update, context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text("اسمت چیه ؟")
    return NAME

async def get_name (update: Update, context: ContextTypes.DEFAULT_TYPE) :
    context.user_data["name"] = update.message.text
    await update.message.reply_text("چند سالته ؟")
    return AGE

async def get_age (update: Update, context: ContextTypes.DEFAULT_TYPE) :
    context.user_data["age"] = update.message.text
    await update.message.reply_text(f'salam {context.user_data["name"]} to {context.user_data["age"]} salet hast.')
    return ConversationHandler.END






app = ApplicationBuilder().token(TOKEN).build()


conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start)
    ],

    states={
        NAME: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_name
            )
        ],

        AGE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_age
            )
        ]
    },

    fallbacks=[]
)

app.add_handler(conv_handler)

print("ربات روشن شد...")

app.run_polling()