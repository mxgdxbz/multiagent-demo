#! /usr/bin/bash

export API_KEY="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"

if [ "$#" -gt 1 ]; then
  echo "Error: Too many arguments provided. Only one argument is allowed."
  exit 1
fi

APP_DIR=${1:-./app} # Use the first argument as the directory or default to ./app
autogenstudio ui --port 8081 --appdir "$APP_DIR"
