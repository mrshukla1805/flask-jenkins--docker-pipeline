from alpine:latest

RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN apk add --update --no-cache g++ gcc libxslt-dev

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]