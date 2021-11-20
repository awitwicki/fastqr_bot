import os
import re
import requests
from telegram import ParseMode
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
import datetime
from logs import logger
from amzqr import amzqr

# t.me/fastqr_bot
bot_token = os.getenv('FASTQR_TOKEN')
influx_query_url = os.getenv('FASTQR_INFLUX_QUERY')

#regex for match text to qr
regex_url = "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"

start_msg = 'Привет, меня зовут @fastqr\\_bot, я помогу тебе быстро и просто создать красивые qr коды.\n\nДля создания простого qr-кода - напиши мне ссылку на любой веб ресурс, например:\n`github.com` или\n`https://github.com`\n\n**Допускается максимальная длина ссылки 400 символов латинницей.**\n\nДля создания qr-кода с картинкой в фоне необходимо прислать в одном сообщении картинку с описанием (в описании картинки просто впиши ссылку)\n\nСсылка на гитхаб github.com/awitwicki/fastqr\\_bot'
error_msg = 'Допускаются только ссылки на любой веб ресурс, например:\n`github.com` или\n`https://github.com`\n\n**Максимальная длина ссылки 400 символов латинницей.**'
error_msg_photo = 'Для создания qr-кода с картинкой в фоне необходимо прислать в одном сообщении картинку с описанием (в описании картинки просто впиши ссылку)'


def influx_query(query_str: str):
    if influx_query_url:
        try:
            url = influx_query_url
            headers = {'Content-Type': 'application/Text'}

            x = requests.post(url, data=query_str.encode('utf-8'), headers=headers)
        except Exception as e:
            print(e)


def make_qrfile(text, photo = None):
    filename = datetime.datetime.utcnow().strftime('img/%Y%m%d_%H%M%S.%f')[:-3] + '.png'

    version, level, qr_name = amzqr.run(
        text,
        version=1,
        level='H',
        picture=photo,
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=filename,
        save_dir=os.getcwd()
    )

    return filename


def start(update, context):
    user = update.message.from_user
    logger.info(f"{user.first_name} has started bot")
    update.message.reply_photo(photo=open('logo.jpg', 'rb'), caption = start_msg, parse_mode=ParseMode.MARKDOWN)


def makeqr_photo(update, context):
    global regex_url
    user = update.message.from_user
    text = update.message.caption.lower()
    influx_query('bots,botname=fastqr,actiontype=message action=true')

    #check antiflood message length and match regex filter
    if text and len(text) < 400 and re.match(regex_url, text):
        logger.info(f"User {user.first_name} has sended photo with caption {text}")

        #download photo
        photo_file = update.message.photo[-1].get_file()
        photo_name = datetime.datetime.utcnow().strftime('covers/%Y%m%d_%H%M%S.%f')[:-3]+ '.jpg'
        photo_file.download(photo_name)

        #make qr with photo
        qr_filename = make_qrfile(text, photo_name)

        #send qr image
        update.message.reply_photo(photo=open(qr_filename, 'rb'))
    else:
        replytext = f'{error_msg_photo}\n\n{error_msg}'
        update.message.reply_text(replytext, parse_mode=ParseMode.MARKDOWN)


def makeqr_text(update, context):
    user = update.message.from_user
    text = update.message.text.lower()
    influx_query('bots,botname=fastqr,actiontype=message action=true')

    #check antiflood message length and match regex filter
    if text and len(text) < 400 and re.match(regex_url, text):
        logger.info(f"User {user.first_name} has sended text {text}")

        #make qr
        qr_filename = make_qrfile(text)

        #send qr image
        update.message.reply_photo(photo=open(qr_filename, 'rb'))
    else:
        logger.info(f"User {user.first_name} has sended wrong text {'none' if text is None else text}")
        update.message.reply_text(error_msg, parse_mode=ParseMode.MARKDOWN)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    logger.info(f"Application started")

    # create folders
    if not os.path.exists('img'):
        os.makedirs('img')
        logger.info(f"Created dir /img")

    if not os.path.exists('covers'):
        os.makedirs('covers')
        logger.info(f"Created dir /covers")

    #setup telegram bot
    updater = Updater(bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # message handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(MessageHandler(Filters.text, makeqr_text))
    dp.add_handler(MessageHandler(Filters.photo, makeqr_photo))

    # log all errors
    dp.add_error_handler(error)

    logger.info(f"Starting bot")

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()