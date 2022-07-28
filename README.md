# cms_blogs-new
A basic CMS system running on PostgreSQL.
This database has a schema named ‘CMS’ and a table named ‘Blogs’.
These columns should be: - Id, Author, Published On, Blog Text, Created On
A member of the team has asked for several CSV files to be created.
Each CSV file should be a unique CSV file in the following format:

# Docker postgres container:
docker run --name cms-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres@sql -d postgres

# Database creation:
CREATE DATABASE CMS;
\connect cms;
CREATE SCHEMA CMS;


# Volume creation

 docker volume create output
 

# Docker container creation:
docker build -t cms-blogs .
docker run -it --rm --name cms-test01 -v output:/data  cms-blogs /bin/bash
