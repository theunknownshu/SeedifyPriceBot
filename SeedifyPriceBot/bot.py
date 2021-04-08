import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_prices


telegram_bot_token = "1665334959:AAHrZHo4LjMNTuD5R4BqJ3YVqG-f4FUraTE"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def price(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["price_BNB"]
        price = crypto_data[i]["price"]
        message += f"1 SFUND (Currently showing ADA Price) = \n${price:,.2f} USD\n{change_hour:.3f}% 1 Hour Change\n{change_day:.3f}% Daily Change\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("price", price))
updater.start_polling()
