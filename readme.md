Japankitty
---
Python version based on Django

# Prerequisites
```python
# install required packages, use pip, pip3 or your favorite package manager
pip3 install Django
```

# How to start from 0
```python
# (re)create database
python manage.py makemigrations
python manage.py migrate

# add superuser both for django and japankitty
python manage.py createsuperuser
```
* Then manually add data to database (see import.sql)

# DB exists
Simple instruction how to get things running

```python
python manage.py runserver
```

# Endopints that doesn't require authentication
Trailing / is very important

* `/jk/api/v1/courses/`
* `/jk/api/v1/vocabulary/<id>/`
* `/jk/api/v1/kanji/<id>/`