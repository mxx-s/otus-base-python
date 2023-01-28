FROM tiangolo/uwsgi-nginx-flask:python3.10

COPY ../requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# CMD flask init_db_data