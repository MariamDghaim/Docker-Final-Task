FROM python:3.7-alpine

#container working directory.
WORKDIR /code

#copy the requirements.txt -  each row is a layer
COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

# application port.
EXPOSE 5000

# Copy the python code.
COPY . .

CMD ["flask", "run"]
