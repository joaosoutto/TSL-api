# Welcome to The Silver Wall - Api

![TSL](https://user-images.githubusercontent.com/60697947/150019275-62dc0dcc-c846-45bf-9e6b-4497f78b2b94.png)

# About

_This application is the Api that populates The Silver Wall - Client._

_With it you can create accounts, login, post on the wall, edit and delete posts._

## Built with

- <p style="display:flex;align-items:center;gap:6px;">Python <a href="https://www.python.org/" target="_blank" rel="noreferrer"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="react" style="margin-top:6px;" width="20" height="20"/> </a> </p>

- <p style="display:flex;align-items:center;gap:6px;">Django <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-original.svg" alt="typeScript" style="margin-top:6px;" width="20" height="20"/> </a> </p>

<h1 style="margin-top: 40px;">Requirements</h1>

- \_Please note that this project was developed in Django, so you must have Python installed on your machine to run it. If you don't have it, download it now from the <a href="https://www.python.org/" target="_blank" rel="noreferrer">official Python website</a>.

- \_You will also need The Silver Wall - Client running on your machine to access the front-end app! But don't worry, you can access it <a href="https://github.com/joaosoutto/TSL-client" target="_blank" rel="noreferrer">here</a>.

<h1 style="margin-top: 40px;">Getting Started</h1>

1. Clone repo:

```bash
# SSH
git clone git@github.com:joaosoutto/TSL-api.git

# HTTPS
git clone https://github.com/joaosoutto/TSL-api.git
```

2. Enter in project folder:

```bash
cd TSL-api
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

```bash
. venv/bin/activate
```

5. With the virtual env active, install the dependencies:

```bash
pip install -r requirements.txt
```

6. Execute migrations:

```bash
python manage.py migrate
```

7. Then, run the project:

```bash
python manage.py runserver
```

Note that the project is running in port 8000.
