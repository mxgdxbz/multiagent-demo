#!/bin/bash

# usage:
# to encrypt: ./decrypt_key.sh encrypt $OPENROUTER_API_KEY "your_password"
# to decrypt: ./decrypt_key.sh "your_password"

# Check arguments
if [ "$1" = "encrypt" ] && [ $# -eq 3 ]; then
    # Write string to file and encrypt it
    echo -n "$2" > temp.txt
    openssl enc -aes-256-cbc -pbkdf2 -a -salt -pass pass:"$3" -in temp.txt > key.encrypted
    rm temp.txt
else
    # Write encrypted string to file and decrypt it
    echo -e "\n API KEY: \n\n"
    openssl enc -aes-256-cbc -pbkdf2 -a -d -salt -pass pass:"$1" -in key.encrypted
    echo -e "\n\n"
fi