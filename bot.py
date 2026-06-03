
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
    [InlineKeyboardButton("جمع", callback_data="+"),
     InlineKeyboardButton("تفریق", callback_data="-")],
    [InlineKeyboardButton("ضررب", callback_data="*"),
     InlineKeyboardButton("تقسیم", callback_data="/")]
]

markup = InlineKeyboardMarkup(keyboard)

NUM1, OP, NUM2 = range(3)

async def start (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("عدد اول را وارد کنید :")
    return NUM1


async def get_num1 (update: Update, context: ContextTypes.DEFAULT_TYPE):
    num1 = update.message.text
    if num1.isdigit() :
        context.user_data["num1"] = int(num1)
        await update.message.reply_text("نوع عملیات رو  مشخص کنید:", reply_markup=markup)
        return OP

    else :
       await update.message.reply_text("لطفا فقط عدد وارد کنید")
       return NUM1
    

async def get_op (update: Update, context: ContextTypes.DEFAULT_TYPE) :
    query = update.callback_query
    await query.answer()
    if query == "+" or "-" or "*" or "/" :
        context.user_data["op"] = query
        await update.message.reply_text("عدد دوم را وارد کنید :")
        return NUM2
    else:
        await update.message.reply_text("عملیات  انتخاب شده صحیح نیست دوباره انتخاب کنید")
        return OP
    


async def get_num2 (update: Update, context: ContextTypes.DEFAULT_TYPE):
    num2 = update.message.text
    if num2.isdigit() :
        context.user_data["num2"] = int(num2)

        match(context.user_data["op"]):
            case("+"):
                result = context.user_data["num1"] + context.user_data["num2"]
            case("-"):
                result = context.user_data["num1"] - context.user_data["num2"]
            case("+"):
                result = context.user_data["num1"] * context.user_data["num2"]
            case("+"):
                result = context.user_data["num1"] / context.user_data["num2"]

        await update.message.reply_text(f"نتیجه محاسبه : {result}")
        return ConversationHandler.END

    else :
       await update.message.reply_text("لطفا فقط عدد وارد کنید")
       return NUM2 



async def cancel (update: Update, context: ContextTypes.DEFAULT_TYPE):
       await update.message.reply_text("عملیات لغو شد")
       return ConversationHandler.END  


app = ApplicationBuilder().token(TOKEN).build()


conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start)
    ],

    states={
        NUM1: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_num1)
        ],

        OP: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_op)
        ],

        NUM2: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_num2)
        ]

    },

    fallbacks= [
        CommandHandler("cancel", cancel)
    ]
 
)


app.add_handler(conv_handler)


print("ربات روشن شد...")
app.run_polling()






