FROM python:3.10-bullseye
ADD . /flask
WORKDIR /flask
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "-u", "main.py"]