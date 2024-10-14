#!/bin/sh

# if [[ -z "$string" ]]; then
#     echo "String is empty"
# elif [[ -n "$string" ]]; then
#     echo "String is not empty"
# fi

# if grep -q 'sudo apt update' ~/.zsh_history; then
#     echo "sudo apt update command found in bash history"
# else
#     echo "sudo apt update command not found in bash history"
# fi


# syntax : if [ condition ]; then 
# commands to execute 
# fi
# operator : =, !=, <, >, -eq, -ne, -lt, -le, -gt, -ge

number1=20
number2=30

if [ "$number1" -eq "$number2" ]; then
    echo "Both numbers are equal"
else
    echo "Both numbers are not equal"
fi


# -e FILE : check if the file exists
# -r FILE : check if the file is readable
# -w FILE : check if the file is writable
# -x FILE : check if the file is executable
# -d FILE : check if the file is a directory
# -s FILE : check if the file is not empty
# -f FILE : check if the file is a regular file
# -L FILE : check if the file is a symbolic link

FILE="note.txt"

if [ -f "$FILE" ]; then
    echo "$FILE exsits and is a regular file."
else
    echo "$FILE does not exist or is not a regular file."
fi



# Define the file path
FILE_PATH="$HOME/program/cyber-security/python/note.txt"

# Check if the file exists
if [ -e "$FILE_PATH" ]; then
    echo "File exists."
else
    echo "File does not exist."
fi

# Check if it's a directory
if [ -d "$FILE_PATH" ]; then
    echo "It's a directory."
else
    echo "It's not a directory."
fi

# Check if it's a regular file
if [ -f "$FILE_PATH" ]; then
    echo "It's a regular file."
else
    echo "It's not a regular file."
fi

# Check if the file is writable
if [ -w "$FILE_PATH" ]; then
    echo "File is writable."
else
    echo "File is not writable."
fi

# Check if the file is readable
if [ -r "$FILE_PATH" ]; then
    echo "File is readable."
else
    echo "File is not readable."
fi

# Check if the file is executable
if [ -x "$FILE_PATH" ]; then
    echo "File is executable."
else
    echo "File is not executable."
fi
