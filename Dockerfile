FROM python:3.8-slim-bullseye
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN pip install python-decouple

COPY . . 

CMD ["python", "-c", "from decouple import config; import bot; bot.run(config('DISCORD_TOKEN'))"]