#!/bin/bash


greeting="Welcome to the Greeting System"

# Display the greeting message
echo "$greeting"
echo "Length : ${#greeting}"

# replacement string
word="this is my sister."

# replace 'this is my sister.' with 'this is my brother.'
echo "${word/sister/brother}"

message="cat cat cat"
new_message="${message//cat/dog}"  # Replaces all occurrences of "cat" with "dog"
echo "$new_message" 

# String Splitting
string="This is a sample string"
# array=($(echo "$string" | tr " " "\n"))
IFS=' ' read -r -a array <<< "$string"

echo "Array Length: ${#array[@]}"
echo "First Element: ${array[0]}"
echo "Last Element: ${array[-1]}"


# change case
echo "Uppercase: ${greeting^^}"
echo "Lowercase: ${greeting,,}"

# Trimming whitespace 
word="     h3llo, w0rld!    "
trimmed=$(echo "$word" | sed 's/^ *//;s/ *$//')
echo "Trimmed Word: $trimmed"

# Parameter expansion
trimmed="${word#"${word%%[![:space:]]*}"}" # Trim leading spaces
trimmed="${trimmed%"${trimmed##*[![:space:]]}"}" # Trim trailing spaces
echo "Trimmed Word : $trimmed"

#Escaping Special Characters
string="This is a \$100 string."
echo "$string"