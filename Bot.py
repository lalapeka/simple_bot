import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                  level=logging.INFO,
                  filename='bot.log'
                  )


def start_bot(update: Updater, context: CallbackContext):
    mytext = """Привет, {}

   """.format(update.message.chat.first_name)
    logging.info('User {} press /start'.format(update.message.chat.username))

    update.message.reply_text(mytext)
    logging.info(mytext)

def chat(update, context):
    text = update.message.text.lower()

    if text == "привет":
        response = "Привет! Как дела?"
    elif text == "Нормально":
        response = "Ну и иди нахуй тогда, чмо"
    elif text == "Хорошо":
        response = "Жаль, думал ты помер"
    elif text == "Почему?":
        response = "А это тебя ебать не должно, ок?"
    elif text == "ок":
        response = "Ну вот и порешили"
    else:
        response = "Заебал блять, пиши сука нормально уебан"

    logging.info("User {} sent message: {}".format(update.message.chat.username, text))
    logging.info("Bot responded with message: {}".format(response))
    
    update.message.reply_text(response)    

def main():
    updr = Updater(settings.TOKEN_TELEGRAMM)
    updr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updr.start_polling()
    updr.idle()

if __name__ == "__main__":
    logging.info('Bot started!')
    main()

