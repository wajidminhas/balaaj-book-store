FROM python:3.12
WORKDIR /code
LABEL email="shanitent667@gmail.com"
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/
RUN pip install poetry
COPY . /code/
RUN poetry config virtualenvs.create false

RUN poetry install
EXPOSE 8000:8000
ENTRYPOINT [ "poetry", "run", "uvicorn", "balaaj_book_centre.main:app", "--host", "0.0.0.0", "--reload" ]

