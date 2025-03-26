#!/bin/bash

# python setup
uv venv
source .venv/bin/activate
echo "export PATH=$PATH" >> ~/.bashrc
echo 'source $(pwd)/.env' >> ~/.bashrc

uv pip install -r requirements.txt
git config --global --add safe.directory /workspaces/multiagent-demo

