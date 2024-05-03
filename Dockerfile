FROM python:3.8-slim-buster
WORKDIR /app2
COPY . .
RUN pip install -r requirements.txt
CMD ["python2","app2.py"]
