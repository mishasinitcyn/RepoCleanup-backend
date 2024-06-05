#!/bin/bash

VENV_DIR="venv"

# Check if the virtual environment directory already exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists in $VENV_DIR"
else
    # Create a virtual environment
    python -m venv $VENV_DIR
    echo "Virtual environment created in $VENV_DIR"

    # Activate the virtual environment
    source $VENV_DIR/bin/activate
    echo "Activated virtual enviroment"

    # Upgrade pip to the latest version
    pip install --upgrade pip
    echo "Pip upgraded to the latest version"

    echo "Backend setup complete"
fi

