# Rockets

## Installation

```
pip install flask
pip install validate_email

export FLASK_APP=app.py
flask initdb
```

## Run for development

```
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```

## Run for production

```
export FLASK_APP=app.py
flask run --host=0.0.0.0
```
