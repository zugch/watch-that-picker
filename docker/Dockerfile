FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY src /app/src/

CMD ["python", "app/src/watch.py"]
