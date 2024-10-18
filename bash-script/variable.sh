#!/bin/bash

# Define variables
NAME="jing ling"
echo "Hello, $NAME"

# Define variables with a default value
echo "Hello ${NAME2:-Guest}"

# Print the date
CURRENT_DATE=$(date)
echo "Today is: $CURRENT_DATE"

# Define a readonly variable
readonly PI=3.14

# Array definition and access
array=(apple banana cherry)
echo "Array length: ${#array[@]}"
echo "First element: ${array[0]}"

# Unset is used to remove a variable from memory
unset NAME
echo "Atfer using 'unset' Name is now: ${NAME:-Guest}"

# Function to demonstrate local variables
my_function() {
    local LOCAL_VARIABLE="local variable"
    
    # Check if the local variable is set
    if [ -n "$LOCAL_VARIABLE" ]; then
        echo "Local variable is set"
    else
        echo "Local variable is not set"
    fi
}

# Call the function
my_function
