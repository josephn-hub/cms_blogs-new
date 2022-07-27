# cms_blogs-new

# Docker postgres container:
docker run --name cms-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres@sql -d postgres

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

# Volume creation

 docker volume create output
 

# Docker container creation:
docker build -t cms-blogs .
docker run -it --rm --name cms-test01 -v output:/data  cms-blogs /bin/bash
