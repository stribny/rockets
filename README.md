# Rockets

## Installation

**Rockets** is written for Python 3

```
# inside the folder
pip install -r requirements.txt

export FLASK_APP=app.py
mkdir instance
flask initdb
```

## Run for development

```
# inside the folder
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```

## Run for production

Run using WSGI server such as [gunicorn](http://gunicorn.org):


```
# inside the folder
gunicorn app:app&
```

and setup a reverse proxy for port 8000, e.g. using Nginx.
