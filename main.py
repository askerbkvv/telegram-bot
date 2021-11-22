import re
from telegram import Update, message
from telegram.ext import (
    CallbackContext, 
    Updater, 
    updater, 
    Filters,
    CommandHandler, 
    MessageHandler,
    PicklePersistence, 
)
from menu import main_menu_keyboard
from credentials import TOKEN
import google
from google import googletrans
# from google import text
# import google
from papachons import gogo



def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEDSXVhkiJkkSxkyVE7pfiq1W5R8QeCMQACNAEAAlKJkSMTzddv9RwHWCIE'
    )
    update.message.reply_text(
        "Привет {username} \n\nМеня зовут Свен, я переводчик бот.\nЧто бы понять как я работаю нажми на комманду /help". format(
            username=update.effective_user.first_name\
                if update.effective_user.first_name is not None\
                    else update.effective_user.username),
        reply_markup=main_menu_keyboard()
    )

def pomosh(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEDTiphlMNmpYtDkDx4Mp6SjCrKhHH9JgACSQEAAlKJkSOCWc0kb3d0MyIE'
    )
    update.message.reply_text(
        " Так, изначально я перевожу любое слово на русский\nЕсли хочешь изменить язык перевода смотри на пример\n\n> Пример:\n \t  en: Я все еще учусь \n \t   I am still studying \n >'en:'-это язык на который я переведу \n >'Я все еще учусь'-то что ты хочешь перевести \n\n Чтобы увидеть другие языки, попробуй команду /lang.\n"
    )


def lang(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEDTixhlMO5IQ_99dGAzLUF-R7QlHtQcwACMQEAAlKJkSNy74zuyFRhcyIE'
    )
    update.message.reply_text(gogo)



# def patrik(update: Update, context: CallbackContext):
#     context.bot.send_sticker(
#         chat_id=update.effective_chat.id,
#         sticker='CAACAgIAAxkBAAEDTixhlMO5IQ_99dGAzLUF-R7QlHtQcwACMQEAAlKJkSNy74zuyFRhcyIE'
#     )
#     update.message.reply_text("Не удалось первести. 🛑\nПопробуйте команду /help для получения рекомендции.")



def translateText(update: Update, contex: CallbackContext):
    print(update.message.text)
    if update.message.text is not None:
        reply = google.translateText(update.message.text,update.effective_user.username)
    update.message.reply_text(
        reply
    )


updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', pomosh))
updater.dispatcher.add_handler(CommandHandler('lang', lang))
# updater.dispatcher.add_handler(MessageHandler(google.translateText(), patrik))
updater.dispatcher.add_handler(MessageHandler(Filters.text, translateText))


updater.start_polling()
updater.idle()












