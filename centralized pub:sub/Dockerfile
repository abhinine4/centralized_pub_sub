FROM python:3.8-slim-buster

WORKDIR /dapp
ADD . /dapp
RUN pip install -r requirements.txt

CMD ["python","app.py"]