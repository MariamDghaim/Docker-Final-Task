FROM python:3.7-alpine

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers

#copy the requirements.txt -  each row is a layer
COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

# application port
EXPOSE 5000

# Copy the python code
COPY . .

CMD ["flask", "run"]
