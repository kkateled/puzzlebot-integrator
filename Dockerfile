FROM python:3.10

WORKDIR /

COPY . .

CMD [ "python", "app" ]d