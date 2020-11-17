FROM python:3.6
RUN mkdir /backend
WORKDIR /backend
ADD requirements.txt /backend/
RUN pip3 install --upgrade pip
RUN apt-get update
RUN apt-get install build-essential
RUN apt-get -y install cmake
RUN apt-get -y install libgtk-3-dev
RUN apt-get -y install libboost-all-dev
RUN apt-get -y install cron
RUN pip3 install -r requirements.txt
ADD . /backend/
COPY start /etc/cron.d/start
RUN chmod 0744 /etc/cron.d/start
RUN crontab /etc/cron.d/start
EXPOSE 3000
CMD gunicorn --certfile=/ai/fullchain.pem --keyfile=/ai/privkey.pem --workers=2 --bind=0.0.0.0:3000 backend.wsgi:application
