FROM python:3.7.2

#TODO Not sure which dir is the best for this project yet
ENV APP_PATH /opt/apps

# Set up token adn secret for line_bot_app
ARG YOUR_CHANNEL_ACCESS_TOKEN
ENV YOUR_CHANNEL_ACCESS_TOKEN=$YOUR_CHANNEL_ACCESS_TOKEN
RUN echo $YOUR_CHANNEL_ACCESS_TOKEN
ARG YOUR_CHANNEL_SECRET
ENV YOUR_CHANNEL_SECRET=$YOUR_CHANNEL_SECRET
RUN echo $YOUR_CHANNEL_SECRET

COPY . $APP_PATH/
RUN pip install --no-cache-dir -r $APP_PATH/requirements.txt
#For postgre
RUN pip install psycopg2
#For debugging
RUN apt update && apt install -y vim

WORKDIR $APP_PATH

RUN python manage.py collectstatic --noinput
