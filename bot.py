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
ADD_TASK , DELETE_TASK = range(2)

keyboard = [
    [KeyboardButton("➕ افزودن کار")],
    [KeyboardButton("📋 نمایش کارها")],
    [KeyboardButton("🗑 حذف همه کارها"),
     KeyboardButton("❌ حذف کار مد نظر")]
]

markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if "tasks" not in context.user_data:
              context.user_data["tasks"] = []

        await update.message.reply_text(
              "یک گزینه انتخاب کن:",
              reply_markup=markup
              )





async def start_add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
       await update.message.reply_text(
              "کار مورد نظر را وارد کن:"
       )
       return ADD_TASK

async def save_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
       task = update.message.text
       context.user_data["tasks"].append(task)
       await update.message.reply_text(
        "کار اضافه شد ✅"
               )

       return ConversationHandler.END



async def display(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.user_data.get("tasks"):
        await update.message.reply_text("هیچ کاری ثبت نشده است.")
        return ConversationHandler.END

    else:
        task_text = "\n".join(
            f"{index}. {task}"
            for index, task in enumerate(
                context.user_data["tasks"],
                start=1
            )
        )

        await update.message.reply_text(task_text)
        return ConversationHandler.END



async def delight_all_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
      if context.user_data["tasks"] != [] :
            context.user_data["tasks"] = []
            await update.message.reply_text( "همه کارها حذف شدند")

      else:
            await update.message.reply_text( "هیچ کاری برای حذف وجود ندارد")



async def get_index(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.user_data["tasks"]:
        await update.message.reply_text(
            "هیچ کاری برای حذف وجود ندارد"
        )
        return ConversationHandler.END

    task_text = "\n".join(
        f"{index}. {task}"
        for index, task in enumerate(
            context.user_data["tasks"],
            start=1
        )
    )

    await update.message.reply_text(
        f"""لیست کارها:

{task_text}

شماره کاری که می‌خواهی حذف شود را وارد کن:
"""
    )

    return DELETE_TASK

async def delete_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
      if not update.message.text.isdigit():
        await update.message.reply_text("فقط شماره وارد کنید")
        return DELETE_TASK
      
      else:
              index = int(update.message.text)-1
              if 0 <= index < len(context.user_data["tasks"]):
                     context.user_data["tasks"].pop(index)
                     await update.message.reply_text(
                            "کار مدنظر حذف شد"
                     )
                     return ConversationHandler.END

              else:
                     await update.message.reply_text(
                            "شماره کار مد نظر وجود ندار دوباره امتحان کنید"
                     )
                     return DELETE_TASK


app = ApplicationBuilder().token(TOKEN).build()
       

add_task_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Regex("^➕ افزودن کار$"),
            start_add_task
        )
    ],

    states={
        ADD_TASK: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                save_task
            )
        ]
    },

    fallbacks=[]
)

delete_task_handler = ConversationHandler(
      entry_points=[
            MessageHandler(
                  filters.Regex("^❌ حذف کار مد نظر$"),
                  get_index
            )
      ],

      states={
          DELETE_TASK : [
                MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                delete_task      
                )
          ]  
      },

      fallbacks=[]

)





app.add_handler(
   CommandHandler("start", start)    
)

app.add_handler(add_task_handler)

app.add_handler(
      MessageHandler(
            filters.Regex("^📋 نمایش کارها$"),
            display
      )
)

app.add_handler(
      MessageHandler(
            filters.Regex("^🗑 حذف همه کارها$"),
            delight_all_task
      )
)

app.add_handler(delete_task_handler)






print("ربات روشن شد...")
app.run_polling()