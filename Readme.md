## Python Django Auction WebApp
### Setup
This project uses PostgreSQL database connection
- Create virtual environment for python 3.9
- Setup database connection by changing in ScopicTestAuction/settings/py the following dict:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'scopic_db_test',
        'USER': 'postgres',
        'PASSWORD': '111111',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
### Run commands in terminal:
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

Then run the command to populate database:
- python manage.py create_script

Once the user is created, run the server and access admin part on with the superuser account:
http://127.0.0.1:8000/admin

Pages:
- Homepage: http://127.0.0.1:8000/home
- Registration: http://127.0.0.1:8000/register
- Login: http://127.0.0.1:8000/admin