# Django REST API's with Django Rest Framework

- Django Docs: https://docs.djangoproject.com/en/3.2/
- Django Rest Framework: https://www.django-rest-framework.org/


## Included Projects
There are 3 different projects located in separated branch of this git repo.
The installation and running instructions are located in the respective readme files.

1. [django-library](https://github.com/hemanta212/django-rest/tree/django-library): A basic book library app with basic html template and DRF api backend
2. [react-todo](https://github.com/hemanta212/django-rest/tree/react-todo): React.js frontend powered by the django backend api
3. master or [blog-api](https://github.com/hemanta212/django-rest/tree/blog-api): A fully featured blog api powered by DRF


## BLOG API

### FEATURES
- Documentation with Swagger and Redoc
- Basic testing of models with built-in django testing
- Using Viewsets and Routers
- Token authentication and user registration

### Installation
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

#### Running Projects

```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Navigate to the localhost:8000/api/v1/ and you should see post lists endpoint.

Also navigate to localhost:8000/admin/ and login for admin panel to easily create new users and posts.

#### Running Tests

```
$ python manage.py test
```

#### Access Docs
The swagger and redoc docs are hosted at localhost:8000/swagger/ or /redoc/ respectively.

You can also generate a schema yaml file
```
$ python manage.py generateschema > api-schema.yml
```

### Accessing the API
Lets see how we can interact with a running api with httpie. (You may need to install it with pip install httpie)

```
# Registering user
$ http -f post localhost:8000/api/v1/user-auth/registration/ username='test' password1='testpass' password2='testpass'

# Generating token from existing user
$ http -f post localhost:8000/api/v1/user-auth/login/ username='httpie' password='httpiepass'

# Accesing list of users; REPLACE TOKEN FROM PREVIOUS COMMAND!
$ http get localhost:8000/api/v1/user/ AUTHORIZATION:'Token <previous command output key token here>'

# eg. 'Token c9892bb13fe57681a2687057eec4994b94ffd7a5'

# Create a post. You can view your author id with in previous users list
$ http -f post localhost:8000/api/v1/ author=2 title='HTTPIE' body='hello' AUTHORIZATION:'Token <TOKEN HERE>'

# Update a post
$ http -f put localhost:8000/api/v1/1/ author=2 title='Updated title' body='hello world' AUTHORIZATION:'Token <TOKEN HERE>'

```

### REPL support
A django repl can be summoned using;
```
# For python REPL
$ python manage.py shell

# For database shell
$ python manage.py dbshell
```

For eg interacting with models
```
from posts.models import Post
from django.contrib.auth.models import User

#all_users
User.objects.all()

#all_posts
Post.objects.all()

# You can create update and delete posts and users from here as well
```
