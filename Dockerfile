# Docker file, Image, Container
FROM python:3.7
WORKDIR /cms-blogs

COPY requirements.txt .
COPY configuration.ini .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt 


COPY ./app ./app
COPY ./pytests ./pytests
COPY ./data ./data

VOLUME [ "/data" ]

CMD [ "python", "./app/main.py" ; "python", "./pytests/test_utile.py"  ]
