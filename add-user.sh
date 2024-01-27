#!/bin/bash

# Check if all three parameters are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <First Name> <Last Name> <Email Address>"
    exit 1
fi

# Assign input parameters to variables
first_name="$1"
last_name="$2"
email="$3"

# Send POST request with provided parameters
curl -X POST -H "Content-Type: application/json" -d "{\"first_name\": \"$first_name\", \"last_name\": \"$last_name\", \"email\": \"$email\"}" http://localhost:8888/users
