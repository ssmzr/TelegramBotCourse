from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
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
GET_NAME, GET_AGE, GET_COURSE, GET_NEW_PROFILE, GET_NEW_NAME, GET_NEW_AGE, GET_NEW_COURSE = range(7)

keyboard = [
    [KeyboardButton("ثبت")],
    [KeyboardButton("مشاهده اطلاعات من")],
    [KeyboardButton("ویرایش اطلاعات"),
     KeyboardButton("حذف اطلاعات")]
]

keyboard2 = [
    [InlineKeyboardButton("تغیر نام", callback_data="1")],
    [InlineKeyboardButton("تغیر سن", callback_data="2")],
    [InlineKeyboardButton("تغیر دوره آموزشی", callback_data="3")]
]

markup = ReplyKeyboardMarkup(keyboard, resize_keyboard= True)
markup2 = InlineKeyboardMarkup(keyboard2)





async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not "info" in context.user_data:
        context.user_data["info"] = []

    await update.message.reply_text(
        "ربات ثبت نام",
        reply_markup = markup
    )




#ثبت نام 
async def start_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["info"] = []
    await update.message.reply_text(
        "نام خود را وارد کنید:"
        )
    return GET_NAME




async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.strip()
    if name.isalpha() :
        context.user_data["info"].append(name)
        await update.message.reply_text(
            """نام شما ثبت شد
            لطفا سن خود را وارد کنید :"""
        )
        return GET_AGE
    else:
        await update.message.reply_text(
            "ورودی قابل قبول نیست دوباره امتحان کنید"
        )
        return GET_NAME





async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    age = update.message.text.strip()
    if age.isdigit() and 0 < int(age) <= 120 :
        context.user_data["info"].append(int(age))
        await update.message.reply_text(
            """سن شما ثبت شد
           لطفا شماره دوره آموزشی خود را از لیست زیر انتخاب کنید:"""
        )
        await update.message.reply_text(
            """
            1.پایتون
            2.جانگو
            3.ربات تلگرام
            4.هوش مصنوعی
            """
        )

        return GET_COURSE
    else:
        await update.message.reply_text(
            "ورودی قابل قبول نیست دوباره امتحان کنید"
        )
        return GET_AGE
    




async def get_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    course = update.message.text.strip()
    if course.isdigit() and 0 < int(course) < 5 :
        match(course):
            case("1"):
                context.user_data["info"].append("پایتون")
            case("2"):
                context.user_data["info"].append("جانگو")
            case("3"):
                context.user_data["info"].append("ربات تلگرام")
            case("4"):
                context.user_data["info"].append("هوش مصنوعی")

        await update.message.reply_text(
            f"""
                name.   {context.user_data["info"][0]}
                age.    {context.user_data["info"][1]}
                course. {context.user_data["info"][2]}

             """
        )

        return ConversationHandler.END
    
    else:
        await update.message.reply_text(
            "ورودی قابل قبول نیست دوباره امتحان کنید"
        )
        return GET_COURSE




#مشاهده اطلاعات 
async def display(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("info"):
        await update.message.reply_text(
            "چیزی برای نمایش وجود ندارد"
            )
        return ConversationHandler.END
    else:
        await update.message.reply_text(
                f"""
                    profile:

                    name.   {context.user_data["info"][0]}
                    age.    {context.user_data["info"][1]}
                    course. {context.user_data["info"][2]}

                """
            )
        return ConversationHandler.END
    


#تغیر مشخصات
async def edit_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("info"):
        await update.message.reply_text("ابتدا ثبت نام کنید")
        return ConversationHandler.END
    await update.message.reply_text(
        "کدام گزینه  مد نظر را انتخاب کنید",
        reply_markup=markup2
    )
    return GET_NEW_PROFILE

async def get_new_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    match (query.data):
        case("1"):
            await query.message.reply_text(
                "نام جدید را وارد کنید "
             )
            return GET_NEW_NAME
        
        case("2"):
            await query.message.reply_text(
                "سن جدید را وارد کنید "
             )
            return GET_NEW_AGE
        
        case("3"):
            await query.message.reply_text(
                """
               : دوره جدید را وارد کنید 

                1.پایتون
                2.جانگو
                3.ربات تلگرام
                4.هوش مصنوعی
            """
             )
        case _:
                await query.message.reply_text("گزینه نامعتبر")
                return GET_NEW_PROFILE
    return GET_NEW_COURSE
        

async def get_new_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.strip()
    if name.isalpha() :
        context.user_data["info"][0] = name
        await update.message.reply_text(
            "نام جدید ثبت شد"
        )
        return ConversationHandler.END
    else:
        await update.message.reply_text(
            "ورودی قابل قبول نیست دوباره امتحان کنید"
        )
        return GET_NEW_NAME


async def get_new_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    age = update.message.text.strip()
    if age.isdigit() and 0 < int(age) <= 120 :
        context.user_data["info"][1] = int(age)
        await update.message.reply_text(
            "سن جدید شما ثبت شد"
        )
        
        return ConversationHandler.END
    else:
        await update.message.reply_text(
            "ورودی قابل قبول نیست دوباره امتحان کنید"
        )
        return GET_NEW_AGE
    

async def get_new_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    course = update.message.text.strip()
    if course.isdigit() and 0 < int(course) < 5:
        match(course):
            case("1"):
                context.user_data["info"][2] = "پایتون"
            case("2"):
                context.user_data["info"][2] = "جانگو"
            case("3"):
                context.user_data["info"][2] = "ربات تلگرام"
            case("4"):
                context.user_data["info"][2] = "هوش مصنوعی"
            

        await update.message.reply_text(
           "دوره جدید ثبت شدش"
        )

        return ConversationHandler.END
    
    else:
        await update.message.reply_text(
            "ورودی قابل قبول نیست دوباره امتحان کنید"
        )
        return GET_NEW_COURSE
    


#بخش حذف همه اطلاعات
async def delete_profil(update: Update, context: ContextTypes.DEFAULT_TYPE):
     if not context.user_data.get("info"):
        await update.message.reply_text(
            "چیزی برای حذف کردن وجود ندار"
            )
        return ConversationHandler.END
     else:
         context.user_data["info"] = []
         await update.message.reply_text(
            "همه اطلاعات حذف شد"
            )
         return ConversationHandler.END

async def cancel (update: Update, context: ContextTypes.DEFAULT_TYPE):
       await update.message.reply_text("❌ ثبت نام لغو شد.")
       return ConversationHandler.END   



app = ApplicationBuilder().token(TOKEN).build()

set_profile = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Regex("^ثبت$"),
            start_registration
        )
    ],
    states={
        GET_NAME: [
             MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_name     
                )
        ],
        GET_AGE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_age     
                )
        ],
        GET_COURSE: [
             MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_course     
                )
        ]
    },
    fallbacks=[
            CommandHandler("cancel", cancel)
    ]
)

change_profile = ConversationHandler(
    entry_points=[
            MessageHandler(
                 filters.Regex("^ویرایش اطلاعات$"),
                 edit_profile
            )
    ],
    states={
        
        GET_NEW_PROFILE: [
            CallbackQueryHandler(get_new_profile)
        ],
        GET_NEW_NAME: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_new_name     
                )
        ],
        GET_NEW_AGE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_new_age     
                )
        ],
        GET_NEW_COURSE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                get_new_course   
                )
        ]
    },
    fallbacks=[
            CommandHandler("cancel", cancel)    
    ]
)

app.add_handler(
   CommandHandler("start", start)     
)

app.add_handler(set_profile)

app.add_handler(change_profile)

app.add_handler(
    MessageHandler(
        filters.Regex("^مشاهده اطلاعات من$"),
        display
    )
)



app.add_handler(
    MessageHandler(
        filters.Regex("^حذف اطلاعات$"),
        delete_profil
    )
)


print("ربات روشن شد...")
app.run_polling()