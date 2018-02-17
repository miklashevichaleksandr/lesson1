from telegram.ext import Updater, CommandHandler

def main():
    updater = Updater("536305288:AAGTKLPlZytJlj-QUQFnlJgf0h8aKleZQ0E")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    print(update)
    update.message.reply_text(text)

main()