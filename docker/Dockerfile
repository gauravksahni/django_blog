FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_blog
WORKDIR /django_blog
ADD requirements.txt /django_blog/
RUN pip install -r requirements.txt
ADD . /django_blog/
