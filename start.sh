#! /usr/bin/bash

export OPENROUTER_API_KEY="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"

APP_DIR=${1:-./app} # Use the first argument as the directory or default to ./app
autogenstudio ui --port 8081 --appdir "$APP_DIR"
