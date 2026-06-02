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

NAME, FAMILY, AGE ,CITY = range(4)


async def start (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اسمت چیه ؟")

    return NAME



async def get_name (update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    if name.isalpha :
         context.user_data["name"] = name
         await update.message.reply_text("فامیلت؟ ")

         return FAMILY
    
    else :
        await update.message.reply_text("برای وارد کردن اسم فقط از حروف الفبا استفاده کنید")

        return NAME




async def get_family (update: Update, context: ContextTypes.DEFAULT_TYPE):
    family = update.message.text
    if family.isalpha :
         context.user_data["family"] = family
         await update.message.reply_text("چند شالته ؟")

         return AGE
    
    else :
        await update.message.reply_text("برای وارد کردن فامیلی فقط از حروف الفبا استفاده کنید")

        return FAMILY


async def get_age (update: Update, context: ContextTypes.DEFAULT_TYPE):
    age = update.message.text
    if age.isdigit and  0 < int(age) < 120 :
         context.user_data["age"] = age
         await update.message.reply_text(" اسم شهر؟")

         return CITY
    
    else :
        await update.message.reply_text("سن باید در بازه مناسب و فقط از اعداد باشد")

        return AGE


async def get_city (update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text
    if city.isalpha :
        context.user_data["city"] = update.message.text
        await update.message.reply_text(
            f"""
        ✅ ثبت نام با موفقیت انجام شد

        👤 نام: {context.user_data["name"]}
        👤 فامیلی: {context.user_data["family"]}
        🎂 سن: {context.user_data["age"]}
        🏙 شهر: {context.user_data["city"]}
        """
        )

        return ConversationHandler.END

    else:
      await update.message.reply_text("اسم شهر فقط باید از حروف الفبا تشکیل شده باشد")

      return CITY

       
 



    

app = ApplicationBuilder().token(TOKEN).build()

conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("start", start)
    ],

    states = { 
        NAME:[
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)
        ],

        FAMILY:[
        MessageHandler(filters.TEXT & ~filters.COMMAND, get_family)
        ],

        AGE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)

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






