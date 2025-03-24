#! /usr/bin/bash


if [ "$#" -gt 1 ]; then
  echo "Error: Too many arguments provided. Only one argument is allowed."
  exit 1
fi

APP_DIR=${1:-./app} # Use the first argument as the directory or default to ./app
autogenstudio ui --port 8081 --appdir "$APP_DIR"
