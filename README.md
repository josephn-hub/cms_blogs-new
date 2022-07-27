# cms_blogs-new

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

# Docker container creation:
docker build -t cms-blogs .
docker run -it --rm --name cms-test01 -v output:/data  cms-blogs /bin/bash
