FROM python:3.11.4-slim-bullseye

ADD main.py ./

CMD [ "python", "main.py" ]