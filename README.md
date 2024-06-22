# Ube
A full-stack point of sale app for managing orders at a Filipino café

<img src="https://storage.googleapis.com/frankie-esparza-portfolio/gifs/ube.gif" width="500">

## Features 
- Sigin and create new employee acounts
- Add items to orders
- Seat customers at tables
- Mark orders as paid

## Setup
1) Download PostgreSQL (for macs, download the PostgreSQL app - [HERE](https://postgresapp.com/))
2) Download Python
3) Download Pipenv ```pip install pipenv```    
4) Create a Virtual Environment `pipenv install --python "$PYENV_ROOT/versions/<<version_name>>/bin/python"` (replace <<version_name>>)
5) Install dependencies `pipenv install`
6) Create a `.env` file and copy & paste the contents of `.env.example`
7) Create the database:
```sql
cd thyme
psql    
DROP DATABASE ube;
DROP USER ube;  
CREATE USER thyme WITH PASSWORD '<insert-password-here>';    
CREATE DATABASE thyme WITH OWNER ube;
```
8) Seed the database `python database.py`
9) Check that the data is in the database:
```sql
psql
SELECT * FROM orders;
\q
```
10) Start the local server `pipenv run flask run`
