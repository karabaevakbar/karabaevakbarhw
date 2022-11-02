FROM python:3.10

EXPOSE 4000

RUN mkdir -p /opt/services/bot/akbar-bot
WORKDIR /opt/services/bot/akbar-bot

COPY . /opt/services/bot/akbar-bot

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/bot/akbar-bot/main.py"]
