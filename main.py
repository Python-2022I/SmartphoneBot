from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram import Update,ReplyKeyboardMarkup
import os

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    keyboar = ReplyKeyboardMarkup([
        ['🛍 Shop','📦 Cart'],
        ['📞 Contact','📝 About']
    ])
    bot = context.bot
    bot.sendMessage(
        chat_id=chat_id,
        text='Assalomu alaykum botimizga xush kelibsiz',
        reply_markup=keyboar
    )
def shop(update:Update,context:CallbackContext):
    markup = ReplyKeyboardMarkup([['Samsung','Apple'],['Vivo','Redmi and Xiaomi'],['Nokia','Main menu']])
    context.bot.sendMessage(chat_id=update.message.chat_id,text = 'SHOP',reply_markup = markup)
    print(update.message.text)
def cart(update:Update,context:CallbackContext):
    markup = ReplyKeyboardMarkup([['Cart'],['Order'],['Clear cart'],['Main menu']])
    context.bot.sendMessage(chat_id=update.message.chat_id,text = 'CART',reply_markup = markup)
    print(update.message.text)
def contact(update:Update,context:CallbackContext):
    markup = ReplyKeyboardMarkup([['Phone number'],['Address'],['Location'],['Email'],['Main menu']])
    context.bot.sendMessage(chat_id=update.message.chat_id,text = 'Contact',reply_markup = markup)
    print(update.message.text)
def about(update:Update,context:CallbackContext):
    markup = ReplyKeyboardMarkup([['About us'],['About the bot'],['Main menu']])
    context.bot.sendMessage(chat_id=update.message.chat_id,text = 'About',reply_markup = markup)
    print(update.message.text)

updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🛍 Shop'),shop))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 Cart'),cart))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📞 Contact'),contact))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📝 About'),about))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),start))
updater.start_polling()
updater.idle()
