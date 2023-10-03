import os

import requests
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from dotenv import find_dotenv, load_dotenv


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Hello {update.message.from_user.name}')


def main():
    load_dotenv(find_dotenv())
    token_devman = os.environ.get("TOKEN_DEVMAN")
    TG_token = os.environ.get("TG_TOKEN")
    updater = Updater(token=TG_token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()
    headers = {
        'Authorization': token_devman
    }
    url = 'https://dvmn.org/api/long_polling/'
    payload = {
        'timestamp': '1555493856'
    }
    while (True):
        try:
            response = requests.get(url=url,
                                    headers=headers,
                                    params=payload,
                                    timeout=5,
                                    )
            response.raise_for_status()
            print(response.json())
        except requests.exceptions.ReadTimeout as err:
            print(err)
        except requests.exceptions.ConnectionError as err:
            print(err)

if __name__ == '__main__':
    main()
