from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

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
    [KeyboardButton("➕ افزودن کار")],
    [KeyboardButton("📋 نمایش کارها")],
    [KeyboardButton("🗑 حذف همه کارها"),
     KeyboardButton("❌ حذف کار مد نظر")]
]

markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data["tasks"] = []
        await update.message.reply_text(reply_markup=markup)



async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
        match(text):
               case("➕ افزودن کار"):
                      return add_task
               case("📋 نمایش کارها"):
                      return print_tasks
               case("🗑 حذف همه کارها"):
                      return dell_all
               case("❌ حذف کار مد نظر"):
                      return dell_by_index
                      

         


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply("کار مورد نظر را وارد کن:")
    task = update.message.text
    context.user_data["tasks"] += task
    await update.message.reply("به لیست کار ها اضافه شد ✅")


async def print_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
       if context.user_data["tasks"] != [] :
            await update.message.reply_text("لیست کار ها:")
            for index, task in enumerate(context.user_data["tasks"], start=1) :
                    await update.message.reply_text(f"{index}-->{task}")
       else :
             await update.message.reply_text("لیست کارها خالی است.") 


async def dell_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
       context.user_data["tasks"] = []
       await update.message.reply_text("همه کارها حذف شدند.")


async def dell_by_index(update: Update, context: ContextTypes.DEFAULT_TYPE):
       await update.message.reply_text("شماره کاری که میخواهید حذف بشه را وارد کنید :")
       num = update.message.text
       list_task = context.user_data["tasks"]
       list_task.pop(int(num)-1)
       await update.message.reply_text("کار حذف شد.")


        

app = ApplicationBuilder().token(TOKEN).build()


app.add_handler(
   CommandHandler("start", start)    
)


app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        menu_handler
    )
)


print("ربات روشن شد...")
app.run_polling()