## Image api

This app uses Pillow and  [django image-kit](https://django-imagekit.readthedocs.io/en/latest/) for additional image  parsing. 

#### Instalation 
Create virtualenv and activate it
```
virtualenv env
env/Scripts/activate
```
then pip install requirements
```
pip install -r requirements
```

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```
then go to 
```
http://127.0.0.1:8000/api/picture/
```
or to 
```
http://127.0.0.1:8000/swagger/
```