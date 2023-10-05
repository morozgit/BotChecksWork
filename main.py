import argparse
import os
import textwrap

import requests
import telegram
from dotenv import find_dotenv, load_dotenv


def main():
    load_dotenv(find_dotenv())
    parser = argparse.ArgumentParser(description='Бот отправляет уведомления о проверке работ')
    parser.add_argument('chat_id', help='Введите свой чат ID. Узнать можно @userinfobot')
    chat_id = parser.parse_args().chat_id
    
    token_devman = os.environ.get("TOKEN_DEVMAN")
    TG_TOKEN = os.environ.get("TG_TOKEN")
    bot = telegram.Bot(token=TG_TOKEN)
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


if __name__ == '__main__':
    main()
