FROM python:3.10

WORKDIR /code

ARG database_url="postgresql://rsoibackend:thPbc3UBLYLKRU8p9ZUcgCpfFldCtzfu@localhost:5432/persons_tq3y"

ENV DATABASE_URL=$database_url

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]