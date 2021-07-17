FROM python:3-alpine

WORKDIR /opt
RUN python -m pip install --upgrade pip
COPY . /opt
RUN pip install -r requirements.txt

CMD ["python","hackernews.py"]
