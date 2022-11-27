FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /var/app

RUN pip install --upgrade pip & \
    pip install pipenv==2022.11.25


COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system

COPY . .

CMD uvicorn main:app --host 0.0.0.0

# For run this file, use :
# docker run -it -p 8000:8000 app