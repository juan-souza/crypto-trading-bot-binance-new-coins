# API Dockerfile

FROM python:3.9-alpine
RUN mkdir /binance_new_coins
COPY src /binance_new_coins
COPY ./requirements.txt /binance_new_coins/requirements.txt
WORKDIR /binance_new_coins
RUN pip3 install -r requirements.txt
CMD [ "python", "main.py"]
