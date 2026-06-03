from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    CommandHandler,
    ApplicationBuilder,
    CallbackQueryHandler,
    filters
)

TOKEN = "8721747745:AAF5r6fJdxKheM4DKgNKKsg2WMMIoquNJ34"

keyboard = [
    [
        InlineKeyboardButton("جمع", callback_data="+"),
        InlineKeyboardButton("تفریق", callback_data="-")
    ],
    [
        InlineKeyboardButton("ضرب", callback_data="*"),
        InlineKeyboardButton("تقسیم", callback_data="/")
    ]
]

markup = InlineKeyboardMarkup(keyboard)

NUM1, OP, NUM2 = range(3)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("عدد اول را وارد کنید:")
    return NUM1


async def get_num1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num1 = update.message.text

    if num1.isdigit():
        context.user_data["num1"] = int(num1)

        await update.message.reply_text(
            "نوع عملیات را انتخاب کنید:",
            reply_markup=markup
        )

        return OP

    await update.message.reply_text("لطفاً فقط عدد وارد کنید")
    return NUM1


async def get_op(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    context.user_data["op"] = query.data

    await query.message.reply_text(
        "عدد دوم را وارد کنید:"
    )

    return NUM2


async def get_num2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    num2 = update.message.text

    if not num2.isdigit():
        await update.message.reply_text(
            "لطفاً فقط عدد وارد کنید"
        )
        return NUM2

    context.user_data["num2"] = int(num2)

    num1 = context.user_data["num1"]
    num2 = context.user_data["num2"]
    op = context.user_data["op"]

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2

    elif op == "/":
        if num2 == 0:
            result = "تقسیم بر صفر امکان‌پذیر نیست"
        else:
            result = num1 / num2

    await update.message.reply_text(
        f"نتیجه محاسبه: {result}"
    )

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "عملیات لغو شد."
    )
    return ConversationHandler.END


app = ApplicationBuilder().token(TOKEN).build()

conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start)
    ],

    states={
        NUM1: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_num1
            )
        ],

        OP: [
            CallbackQueryHandler(get_op)
        ],

        NUM2: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_num2
            )
        ]
    },

    fallbacks=[
        CommandHandler("cancel", cancel)
    ]
)

app.add_handler(conv_handler)

print("ربات روشن شد...")
app.run_polling()