#!/bin/bash

# Build the project
echo "Building the project....."
python3.11 -m pip install -r reqirements.txt

echo "Make Migration..."
python3.11 manage.py make migrations --noinput
python3.11 manage.py migrate --noinput

echo "Collect Static..."
Python3.11 manage.py collectstatic --noinput --clear
