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

keyboard1 = [
    [
        InlineKeyboardButton("دنیس ریچی", callback_data="1"),
        InlineKeyboardButton("جیمز گاسلینگ", callback_data="2")
    ],
    [
        InlineKeyboardButton("گویدو ون روسوم", callback_data="3"),
        InlineKeyboardButton("بیارن استراستروپ", callback_data="4")
    ]
]


keyboard2 = [
    [
        InlineKeyboardButton("20", callback_data="1"),
        InlineKeyboardButton("14", callback_data="2")
    ],
    [
        InlineKeyboardButton("24", callback_data="3"),
        InlineKeyboardButton("10", callback_data="4")
    ]
]


keyboard3 = [
    [
        InlineKeyboardButton("int", callback_data="1"),
        InlineKeyboardButton("float", callback_data="2")
    ],
    [
        InlineKeyboardButton("list", callback_data="3"),
        InlineKeyboardButton("bool", callback_data="4")
    ]
]


keyboard4 = [
    [
        InlineKeyboardButton("func", callback_data="1"),
        InlineKeyboardButton("define", callback_data="2")
    ],
    [
        InlineKeyboardButton("method", callback_data="3"),
        InlineKeyboardButton("def", callback_data="4")
    ]
]


keyboard5 = [
    [
        InlineKeyboardButton("=", callback_data="1"),
        InlineKeyboardButton("==", callback_data="2")
    ],
    [
        InlineKeyboardButton("===", callback_data="3"),
        InlineKeyboardButton("=:", callback_data="4")
    ]
]


markup1 = InlineKeyboardMarkup(keyboard1)
markup2 = InlineKeyboardMarkup(keyboard2)
markup3 = InlineKeyboardMarkup(keyboard3)
markup4 = InlineKeyboardMarkup(keyboard4)
markup5 = InlineKeyboardMarkup(keyboard5)

QUESTION1, QUESTION2, QUESTION3, QUESTION4, QUESTION5 = range(5)

async def start (update: Update,context: ContextTypes.DEFAULT_TYPE):
    context.user_data["score"]  = 0
    await update.message.reply_text("پایتون توسط چه کسی ساخته شد؟",reply_markup=markup1)

    return QUESTION1



async def get_answer1(update: Update,context: ContextTypes.DEFAULT_TYPE):
     query = update.callback_query
     await query.answer()

     if query.data == "3" :
          context.user_data["score"] +=1
          await query.message.reply_text("✅ پاسخ صحیح")
          await query.message.reply_text("print(2 + 3 * 4) --> ?",reply_markup=markup2)
          return QUESTION2

     else :
        await query.message.reply_text("❌ پاسخ اشتباه")
        await query.message.reply_text("print(2 + 3 * 4) --> ?",reply_markup=markup2)
        return QUESTION2
     


async def get_answer2(update: Update,context: ContextTypes.DEFAULT_TYPE):
     query = update.callback_query
     await query.answer()

     if query.data == "2" :
          context.user_data["score"] +=1
          await query.message.reply_text("✅ پاسخ صحیح")
          await query.message.reply_text("کدام نوع داده برای ذخیره چند مقدار استفاده می‌شود؟",reply_markup=markup3)
          return QUESTION3

     else :
        await query.message.reply_text("❌ پاسخ اشتباه")
        await query.message.reply_text("کدام نوع داده برای ذخیره چند مقدار استفاده می‌شود؟",reply_markup=markup3)
        return QUESTION3




async def get_answer3(update: Update,context: ContextTypes.DEFAULT_TYPE):
     query = update.callback_query
     await query.answer()

     if query.data == "3" :
          context.user_data["score"] +=1
          await query.message.reply_text("✅ پاسخ صحیح")
          await query.message.reply_text("برای تعریف تابع در پایتون از چه کلمه‌ای استفاده می‌شود؟",reply_markup=markup4)
          return QUESTION4

     else :
        await query.message.reply_text("❌ پاسخ اشتباه")
        await query.message.reply_text("برای تعریف تابع در پایتون از چه کلمه‌ای استفاده می‌شود؟",reply_markup=markup4)
        return QUESTION4
     



async def get_answer4(update: Update,context: ContextTypes.DEFAULT_TYPE):
     query = update.callback_query
     await query.answer()

     if query.data == "4" :
          context.user_data["score"] +=1
          await query.message.reply_text("✅ پاسخ صحیح")
          await query.message.reply_text("کدام عملگر برای مقایسه برابری استفاده می‌شود؟",reply_markup=markup5)
          return QUESTION5

     else :
        await query.message.reply_text("❌ پاسخ اشتباه")
        await query.message.reply_text("کدام عملگر برای مقایسه برابری استفاده می‌شود؟",reply_markup=markup5)
        return QUESTION5
     



async def get_answer5(update: Update,context: ContextTypes.DEFAULT_TYPE):
     query = update.callback_query
     await query.answer()

     if query.data == "2" :
          context.user_data["score"] +=1
          await query.message.reply_text("✅ پاسخ صحیح")
          score = int(context.user_data["score"])

          if score == 5 :
              await query.message.reply_text(f"""
                آزمون تمام شد

                امتیاز شما:
                {score}
                از 5 نمره
                                                            
                🏆 عالی

                """)
              
          
          if score in [3, 4]:
              await query.message.reply_text(f"""
                آزمون تمام شد

                امتیاز شما:
                {score}
                از 5 نمره
                                                            
                👍 خوب

                """)
          
              
          if score < 3 :
              await query.message.reply_text("""
                آزمون تمام شد

                امتیاز شما:
                {score}
                از 5 نمره
                                                            
                📚 نیاز به تمرین بیشتر

                """)
          return ConversationHandler.END  


          

     else :
        await query.message.reply_text("❌ پاسخ اشتباه")
        score = int(context.user_data["score"])

        if score == 5 :
            await query.message.reply_text("""
            آزمون تمام شد

            امتیاز شما:
            {score}
            از 5 نمره
                                                        
            🏆 عالی

            """)
            
        
        if score == 3 or score == 4 :
            await query.message.reply_text("""
            آزمون تمام شد

            امتیاز شما:
            {score}
            از 5 نمره
                                                        
            👍 خوب

            """)
            
        if score < 3 :
            await query.message.reply_text("""
            آزمون تمام شد

            امتیاز شما:
            {score}
            از 5 نمره
                                                        
            📚 نیاز به تمرین بیشتر

            """)
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
        QUESTION1 :[
            CallbackQueryHandler(get_answer1)
        ],

         QUESTION2 :[
            CallbackQueryHandler(get_answer2)
        ],

         QUESTION3 :[
            CallbackQueryHandler(get_answer3)
        ],

         QUESTION4 :[
            CallbackQueryHandler(get_answer4)
        ],

         QUESTION5 :[
            CallbackQueryHandler(get_answer5)
        ]
    },

    fallbacks=[
        CommandHandler("cancel", cancel)
    ]
)

app.add_handler(conv_handler)



print("ربات روشن شد...")
app.run_polling()