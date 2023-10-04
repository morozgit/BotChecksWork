# Отправляем уведомления о проверке работ

Бот проверяет выполнение работ на devman
## Установка 

Установите [python3](https://realpython.com/installing-python/).

## Репозиторий
Клонируйте репозиторий в удобную папку.

## Виртуальное окружение
В терминале перейдите в папку с репозиторием.

### Создание виртуального окружения
```python 
python3 -m venv venv
```

### Активация виртуального окружения Linux

```
source venv/bin/activate
```

### Активация виртуального окружения Windows

```
venv\Scripts\activate
```

### Установка библиотек

```python 
pip3 install -r requirements.txt
```

#### Запись токена Telegram
```python
echo TG_TOKEN=ваш токен > .env
```

#### Запись API Девмана
```python
echo TOKEN_DEVMAN=ваш токен >> .env
```

## Запуск

Из директории с проектом запустите сайт командой.
```python
python3 main.py CHAT_ID
```
Узнать CHAT_ID можно [@userinfobot](https://telegram.me/userinfobot).
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
