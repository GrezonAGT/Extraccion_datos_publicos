FROM python:3.12.8

WORKDIR /code

COPY etl.py /code

RUN pip install pandas sodapy psycopg2-binary numpy

CMD ["python", "etl.py"]