#!/bin/bash

# I prefer to use poetry instead pipenv
#source "$(pipenv --venv)"/bin/activate
source "$(poetry env info --path)"/bin/activate

# I prefer to run the manin.py directly and running the flask app in there by
# running the app.run() method
#export FLASK_APP=./src/main.py
#flask run -h 0.0.0.0
python -m src.main
