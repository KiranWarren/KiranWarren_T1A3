#!/bin/bash

# Check if Python is installed
if ! [[ "$(python3 --version)" =~ "Python 3" ]]
    then
        echo "Sorry, python3 command is not working. Please ensure you have Python 3 installed before using this application."
        exit 0
fi

# Check if pip is installed
if ! [[ "$(pip3 --version)" =~ "pip " ]]
    then
        echo "Sorry, pip3 command is not working. Please ensure you have PIP 3 installed before using this application."
        exit 0
fi

# Create virtual environment and set as current environment
python3 -m venv venv
source venv/bin/activate

# Install package requirements into venv
pip3 install cryptography

# Run application
python3 main.py

# Deactivate and remove virtual environment upon exiting application
deactivate
rm -rf venv __pycache__