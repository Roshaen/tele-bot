from telegram import *
from telegram.ext import *

bot = Bot('BOT TOKEN HERE')
update1 = Updater('BOT TOKEN HERE', use_context=True)
dispatcher = update1.dispatcher

def greet(update:Update, context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='Hello there!!!')
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='Welcome to Roshan\'s Bot')
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='Go to github:')
    bot.send_message(chat_id=update.effective_chat.id, 
                        text='https://github.com/roshaen')

start = CommandHandler('start', greet)
dispatcher.add_handler(start)
update1.start_polling()
