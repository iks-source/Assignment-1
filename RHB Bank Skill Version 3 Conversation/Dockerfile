# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Set up environment variables
ENV mongodb_uri="mongodb+srv://watsonbotDB:O2AWLb00wnDI6SDo@convolog.ruvc1yo.mongodb.net/?retryWrites=true&w=majority"
ENV mongodb_db_name="ConversationLogs"
ENV mongodb_collection_name="RHB Bank Skill Conversation Version 3 Log"

ENV redis_host="redis-11493.c295.ap-southeast-1-1.ec2.cloud.redislabs.com"
ENV redis_port=11493
ENV redis_password="qvhFpGRf9fuwFqucW1IabdEoYoN26uS1"

ENV bot_name="RHB Bank Skill Version 3 Conversation:"


# Copy local code to the container image.
# *** Change besca_specific to your bot webhook name
ENV APP_HOME /besca_bot
ENV PORT 8000
WORKDIR $APP_HOME

COPY ./besca_bot ./app/
# WORKDIR ../common_dir

COPY ./common_code ./app/

WORKDIR $APP_HOME/app/

# Install production dependencies.
RUN pip install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 --timeout 0 fastapi_main:app