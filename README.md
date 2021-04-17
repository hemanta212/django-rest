# Django library App

## Installation

**Note**:
Use requirements-dev.txt instead of requirements.txt if you need pylint, black, httpie etc.


- With pip
  - Windows

```
$ python -m venv .venv
$ .venv\Scripts\activate
$ python -m pip install -r requirements.txt
```

  - Unix/Linux
```
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -r requirements.txt
```

- With Poetry

```
$ poetry install 

# Activates virtual environment
$ poetry shell
```

### Running server

```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
Site is hosted at localhost:8000 and 

Api is hosted at localhost:8000/api/

Also navigate to localhost:8000/admin/ and login for admin panel to easily create new books.
