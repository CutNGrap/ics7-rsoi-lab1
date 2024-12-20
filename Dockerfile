FROM python:3.10

WORKDIR /code

ARG database_url="postgresql://pgsql_km2s_user:zL8bxyjG9knQpjPZSDBpdR8TDHosPyV3@dpg-ctit1252ng1s73bf2a60-a.oregon-postgres.render.com/pgsql_km2s"

ENV DATABASE_URL=$database_url

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]