# Отправляем уведомления о проверке работ

Бот проверяет выполнение работ на devman
## Установка 

Установите [python3](https://realpython.com/installing-python/).

## Репозиторий
Клонируйте репозиторий в удобную папку.

## Виртуальное окружение
В терминале перейдите в папку с репозиторием.

### Создание виртуального окружения
```bush 
python3 -m venv venv
```

### Активация виртуального окружения Linux

```bush
source venv/bin/activate
```

### Активация виртуального окружения Windows

```bush
venv\Scripts\activate
```

### Установка библиотек

```bush 
pip3 install -r requirements.txt
```

#### Запись токена Telegram
```bush
echo TG_TOKEN=ваш токен > .env
```

#### Запись API Девмана
```bush
echo TOKEN_DEVMAN=ваш токен >> .env
```

## Запуск

Из директории с проектом запустите сайт командой.
```bush
python3 main.py CHAT_ID
```
Узнать CHAT_ID можно [@userinfobot](https://telegram.me/userinfobot).

## Запуск в Docker
Установить [Docker](https://www.docker.com/get-started/)

Скачать образ 
```bush
docker pull morozdocker/bot_checks_work
```

Запустить 
```bush
docker run morozdocker/bot_checks_work CHAT_ID
```
Узнать CHAT_ID можно [@userinfobot](https://telegram.me/userinfobot).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
