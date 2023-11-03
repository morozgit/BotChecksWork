import argparse
import logging
import os
import textwrap

import requests
import telegram
from dotenv import find_dotenv, load_dotenv


class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def main():
    load_dotenv(find_dotenv())
    parser = argparse.ArgumentParser(description='Бот отправляет уведомления о проверке работ')
    parser.add_argument('chat_id', help='Введите свой чат ID. Узнать можно @userinfobot')
    chat_id = parser.parse_args().chat_id
    
    token_devman = os.environ.get("TOKEN_DEVMAN")
    tg_token = os.environ.get("TG_TOKEN")
    bot = telegram.Bot(token=tg_token)
   
    bot.logger.addHandler(TelegramLogsHandler(bot, chat_id))
    bot.logger.warning('Бот запущен')

    headers = {
        'Authorization': token_devman
    }
    url = 'https://dvmn.org/api/long_polling/'
    while True:
        try:
            response = requests.get(url=url,
                                    headers=headers,
                                    timeout=5,
                                    )
            response.raise_for_status()
            devman_works = response.json()
            for devman_work in devman_works['new_attempts']:
                if devman_work['is_negative']:
                    bot.send_message(chat_id=chat_id, text=textwrap.dedent(f''' 
                                У вас проверили работу "{devman_work['lesson_title']}"\n
                                Ссылка на урок - {devman_work['lesson_url']}\n
                                К сожалению в работе нашлись ошибки
                                '''))
                else:
                    bot.send_message(chat_id=chat_id, text=textwrap.dedent(f''' 
                                У вас проверили работу "{devman_work['lesson_title']}"\n
                                Ссылка на урок - {devman_work['lesson_url']}\n
                                Преподавателю все понравилось, можно приступать 
                                к следующему уроку!
                                    '''))
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError as err:
            print(err)
            continue
        except Exception as err:
            error = f'Бот упал с ошибкой {str(err)}'
            bot.logging.error(error)


if __name__ == '__main__':
    main()
