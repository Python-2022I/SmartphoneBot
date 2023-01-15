from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup, keyboardbutton
import os

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    keyboar = ReplyKeyboardMarkup([
        ['🛍 Shop','📦 Cart'],
        ['Contact','📝 About']
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
def Samsung(update:Update,context:CallbackContext):
    markup = ReplyKeyboardMarkup([['Samsung A class'],['Samsung S class'],['Samsung Note class'],['Samsung Z fold'],['Main menu']])
    context.bot.sendMessage(chat_id=update.message.chat_id,text = 'Samsung',reply_markup = markup)
    print(update.message.text)
def Apple(update:Update,context:CallbackContext):
    markup = ReplyKeyboardMarkup([['Ipad'],['Iphone','Iphone pro'],['Iphone pro max','Main menu']])
    context.bot.sendMessage(chat_id=update.message.chat_id,text = 'SHOP',reply_markup = markup)
    print(update.message.text)
def cart(update:Update,context:CallbackContext):
    markup = ReplyKeyboardMarkup([['Cart'],['Order'],['Clear cart'],['Main menu']])
    context.bot.sendMessage(chat_id=update.message.chat_id,text = 'CART',reply_markup = markup)
    print(update.message.text)
def contact(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Phone number',callback_data='number')],
        [InlineKeyboardButton(text='Address',url='https://google.com')],
        [InlineKeyboardButton(text='Email',callback_data='email')]

    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
def query(update: Update, context: CallbackContext):
    quer=update.callback_query
    quer.answer('Done')
    chat_id=quer.message.chat_id
    bot = context.bot
    if quer.data=='number':
        bot.sendMessage(chat_id,'+998911280552')
    if quer.data=='email':
        bot.sendMessage(chat_id,'ayyubxonhamdamovtatu@gmail.com')
    
def about(update:Update,context:CallbackContext):
    markup = ReplyKeyboardMarkup([['About us'],['About the bot'],['Main manu']])
    context.bot.sendMessage(chat_id=update.message.chat_id,text = 'About',reply_markup = markup)
    print(update.message.text)

updater = Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🛍 Shop'),shop))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 Cart'),cart))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Contact'),contact))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📝 About'),about))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Samsung'),Samsung))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Apple'),Apple))
updater.dispatcher.add_handler(CallbackQueryHandler(query))
updater.start_polling()
updater.idle()
