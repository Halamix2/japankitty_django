Japankitty
---
Python version based on Django

# Prerequisites
```python
# install required packages, use pip, pip3 or your favorite package manager
pip3 install Django django-rest-framework django-oauth-toolkit django-cors-middleware django-braces
```

# How to start from 0
```python
# (re)create database
python manage.py makemigrations
python manage.py migrate

# add superuser both for django and japankitty
python manage.py createsuperuser
```
* go to `http://127.0.0.1:8000/admin` and log in
* go to `http://127.0.0.1:8000/jk/o/applications/` and add new apllication "frontend"(client type: confidential, grant type:password-based). Copy client id and secret, it'll be used to identify application itself

# DB exists
Simple instruction how to get things running

Default superuser is admin/admin.

```python
python manage.py runserver
```