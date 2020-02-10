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
python manage.py makemigrations jk
python manage.py migrate jk

python manage.py makemigrations
python manage.py migrate

# add superuser both for django and japankitty
python manage.py createsuperuser
```
* Then manually add data to database (see import.sql)
* go to `http://127.0.0.1:8000/admin` and log in
* go to `http://127.0.0.1:8000/jk/o/applications/` and add new apllication "frontend"(client type: confidential, grant type:password-based). Copy client id and secret, it'll be used to identify application itself

# DB exists
Simple instruction how to get things running

Default superuser is admin/admin.
```python
python manage.py runserver
```

Client id:
JCyUncgFfufgNUW014WLA7nXw1DkOTbZV5Ritlv0

secret:
e7EZc3x0izr3EfB0r0L1gnoIKe8ckOChujs6LwG882xYWwW3JGo90cW508xLFf9EUPaP8zDKEg76zsh5TqtAamSFn7R0q1aVXg0Aj20nwjpyJZgFS2WtujBmGdDninGh

# Endopints that doesn't require authentication
Trailing / is very important

* `/jk/api/v1/courses/`
* `/jk/api/v1/vocabulary/<id>/`
* `/jk/api/v1/kanji/<id>/`

# Getting user token (a.k.a log-in)
* Send POST at http://localhost:8000/jk/o/token/
* POST data
    * `username: admin`
    * `password: admin`
    * `grant_type: password`
* send basic authentication (not Bearer!), where username is client id and password is client secret, e.g.
    * `username: JCyUncgFfufgNUW014WLA7nXw1DkOTbZV5Ritlv0`
    * `password: e7EZc3x0izr3EfB0r0L1gnoIKe8ckOChujs6LwG882xYWwW3JGo90cW508xLFf9EUPaP8zDKEg76zsh5TqtAamSFn7R0q1aVXg0Aj20nwjpyJZgFS2WtujBmGdDninGh`

Instead of using basic authentication you can also use `client_id` and `client_secret` POST data

In return you'll get something like
```json
{
    "access_token": "JfbwOajwJckM9Qbj3Y0bo74IG1Y0fR",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "PL6axcMnBesxkVBOMlQ0UiAdMP97Wm"
}
```
where `access_token` was called `token` in previous version

# Refreshing token
* Send POST at http://localhost:8000/jk/o/token/
* POST data
    * `refresh_token: 904X5ACEo4MIEpQmTbdky2IEuNnvUv`
    * `grant_type: refresh_token`
* send basic authentication (not Bearer!), where username is client id and password is client secret, e.g.
    * `username: JCyUncgFfufgNUW014WLA7nXw1DkOTbZV5Ritlv0`
    * `password: e7EZc3x0izr3EfB0r0L1gnoIKe8ckOChujs6LwG882xYWwW3JGo90cW508xLFf9EUPaP8zDKEg76zsh5TqtAamSFn7R0q1aVXg0Aj20nwjpyJZgFS2WtujBmGdDninGh`

Instead of using basic authentication you can also use `client_id` and `client_secret` POST data

In return you'll get something like
```json
{
    "access_token": "iJFoTumfVgQZJUNKTxOrBie2zuO8qX",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "r6xihVu7x8nZB1ZIKzxXGYN3nielNO"
}
```

# Revoking token
* Send POST at http://localhost:8000/jk/api/v1/revoke_token/
* POST data
    * `token: 0a1MpxlBYKdy66yk6RcbkKrWhdM9Fb`
* send basic authentication (not Bearer!), where username is client id and password is client secret, e.g.
    * `username: JCyUncgFfufgNUW014WLA7nXw1DkOTbZV5Ritlv0`
    * `password: e7EZc3x0izr3EfB0r0L1gnoIKe8ckOChujs6LwG882xYWwW3JGo90cW508xLFf9EUPaP8zDKEg76zsh5TqtAamSFn7R0q1aVXg0Aj20nwjpyJZgFS2WtujBmGdDninGh`

Instead of using basic authentication you can also use `client_id` and `client_secret` POST data

You won't get any output from that, just status 200, even if it fails

# Registering user
* Send POST at http://localhost:8000/jk/api/v1/revoke_token/
* POST data
    * `username: admin`
    * `password: admin`
    * `email: admin@admin.pl`
    * `grant_type: password`
* send basic authentication (not Bearer!), where username is client id and password is client secret, e.g.
    * `username: JCyUncgFfufgNUW014WLA7nXw1DkOTbZV5Ritlv0`
    * `password: e7EZc3x0izr3EfB0r0L1gnoIKe8ckOChujs6LwG882xYWwW3JGo90cW508xLFf9EUPaP8zDKEg76zsh5TqtAamSFn7R0q1aVXg0Aj20nwjpyJZgFS2WtujBmGdDninGh`

Instead of using basic authentication you can also use `client_id` and `client_secret` POST data

In return you'll get something like
```json
{
    "access_token": "iJFoTumfVgQZJUNKTxOrBie2zuO8qX",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "r6xihVu7x8nZB1ZIKzxXGYN3nielNO"
}
```
