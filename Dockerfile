FROM python:3.9-slim
ENV PYTONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN apt-get update && apt-get install -y python3-opencv
CMD python discord_bot.py
