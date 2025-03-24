#!/bin/bash

# python setup
uv venv
source .venv/bin/activate
echo "export PATH=$PATH" >> ~/.bashrc
uv pip install -r requirements.txt

