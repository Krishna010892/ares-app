FROM python:3.14-alpine

WORKDIR /app

ADD backend/requirement.txt /app/requirement.txt

RUN pip install -r /app/requirement.txt

ADD backend/ /app


ENTRYPOINT ["python"]

CMD ["app.py"]