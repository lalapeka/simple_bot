import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filtres

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                  level=logging.INFO,
                  filename='bot.log'
                  )

def start_bot(update: Updater, context: CallbackContext):
    mytext = """Привет, {}

    Давай сыграем в игру =)""".format(update.message.chat.first_name)
    update.message.reply_text(mytext)

def chat(update: Updater, context: CallbackContext):
    text = "Привет"
    logging.info(text)

    update.message.reply_text(text)    

def main():
    updr = Updater(settings.TOKEN_TELEGRAMM)
    updr.dispatcher.add_handler(CommandHandler("start", start_bot))
        updr.dispatcher.add_handler(MessageHandler(Filtres.text, chat))


    updr.start_polling()
    updr.idle()

if __name__ == "__main__":
    logging.info('Bot started!')
    main()

