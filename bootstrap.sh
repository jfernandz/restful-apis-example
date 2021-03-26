#!/bin/bash

#source "$(pipenv --venv)"/bin/activate
source "$(poetry env info --path)"/bin/activate

#export FLASK_APP=./src/main.py
#flask run -h 0.0.0.0
python -m src.main
