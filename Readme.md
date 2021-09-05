## Python Django Auction WebApp
### Setup
This project uses PostgreSQL database connection
- Create virtual environment for python 3.9
### Run commands in terminal:
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

Once the user is created, run the server and access admin part on:
http://127.0.0.1:8000/admin

Pages:
- Homepage: http://127.0.0.1:8000/home
- Registration: http://127.0.0.1:8000/register
- Login: http://127.0.0.1:8000/admin