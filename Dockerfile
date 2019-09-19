FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV OAUTHLIB_INSECURE_TRANSPORT 1

COPY ./airavata-django-portal.zip /
WORKDIR /
RUN unzip  airavata-django-portal.zip
WORKDIR /airavata-django-portal
RUN pip install -r requirements.txt

EXPOSE 8000

VOLUME /code

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

