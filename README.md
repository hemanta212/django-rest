## React TODO App

### Installation

#### Backend Python-Django

```
$ cd backend
```

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

##### Running server

```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
Api is hosted at localhost:8000/api/

Also navigate to localhost:8000/admin/ and login for admin panel to easily create new users and posts.


#### Frontend Node-React
- Install nodejs (use [nvm](https://github.com/nvm-sh/nvm) on linux).

```
$ cd frontend
$ npm install
$ npm start
```

Navigate to localhost:3000 to see the react app.


#### Running Tests

```
$ python manage.py test
```
