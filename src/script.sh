#!/bin/bash

# Check if Python is installed

# Check if pip is installed

# Create virtual environment and set as current environment
python3 -m venv venv
source venv/bin/activate

# Install package requirements
pip3 install pytest
pip3 install cryptography

# Run 
python3 main.py

# Deactivate and remove virtual environment
deactivate
rm -rf venv