# Try Django
Learn the fundamentals behind one of the most popular web frameworks in the world by building a real project.

Learn the fundamentals behind one of the most popular web frameworks in the world by building a real project. Django has so many features that just work out of the box: user authentication, database management, html template rending, URL routing, form data validation, and so much more.

Django is a web-framework written in Python and runs the backend for many of the internet's most popular websites such as Instagram and Pinterest.

Reference code

### Usage

- Clone git repo

``` bash
git clone git@github.com:shabayekdes/try-django.git
cd try-django
```

- Initialize the project:

``` bash
python3 -m venv .venv
```

- Activate the virtual environment:

``` bash
source .venv/bin/activate
```

- Install collected package from requirements.txt:

``` bash
pip install -r requirements.txt
```

- Generate a one-off secret key in Django

``` bash
cp .env.example .env
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
> copy key and put it on 
DJANGO_SECRET_KEY=

- Run migrate to create databases table

``` bash
cp .env.example .env

python manage.py migrate
```

- Run python web server

``` bash
python manage.py runserver
```
