FROM python:3.11
WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

COPY ./main.py /backend/main.py
COPY ./db.py /backend/db.py
COPY ./db.sqlite3 /backend/db.sqlite3

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10001", "--proxy-headers"]

LABEL org.opencontainers.image.source=https://github.com/Resend1298/bookdb-midterm-backend
