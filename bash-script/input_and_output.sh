#!/bin/bash

# -n Suppresses the trailing newline
echo -n "Hello, "
echo "world"

# -e Enables interpretation of backslash escapes
echo -e "This is a \nmulti-line\tstring"


# using printf command
# syntax : printf "format string" [argument...]
# %s : string
# %d : integer
# %f : float
# %x : hexadecimal

printf "My name is %s and I am %d years old.\n" "jing" 23

# Reading user input
# syntax : read [option] variable
# -p : prompts the user 
# -s : Silent mode ( does not echo input, useful for password )
# -a : read input into an array

echo -n "Enter your name : "
read name
echo "Hello, $name!"

read -p "Enter your email : " email
read -s -p "Enter your password : " password
echo
read -a numbers -p "Enter three numbers separated by spaces : "

echo "Your email is $email"
echo "Your password is $password"
echo "Your numbers are ${numbers[@]}"


