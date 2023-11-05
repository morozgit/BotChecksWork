FROM python:3.10

WORKDIR /bot

COPY requirements.txt /bot/

RUN pip3 install -r requirements.txt

COPY . /bot

CMD ["python", "main.py"]