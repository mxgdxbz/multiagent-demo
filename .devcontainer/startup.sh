#!/bin/bash

# python setup
pushd python
source .venv/bin/activate
echo "export PATH=$PATH" >> ~/.bashrc
popd
