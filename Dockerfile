FROM python:3

WORKDIR /usr/src/app

COPY nlp.py .
COPY requirements.txt .

RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN apt-get install gcc -y


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./nlp.py"]
