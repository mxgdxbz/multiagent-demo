#!/bin/bash

# python setup for codespace
uv venv
source .venv/bin/activate
echo "export PATH=$PATH" >> ~/.bashrc
echo 'source $(pwd)/.env' >> ~/.bashrc

uv pip install -r requirements.txt
uv tool install mcp-server-fetch  # for python based MCP server
git config --global --add safe.directory /workspaces/multiagent-demo
playwright install-deps chrome chromium
playwright install
