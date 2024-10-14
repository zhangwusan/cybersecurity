#!/bin/bash

# for item in list; do

# done

for FRUIT in apple banana cherry; do

    echo "I love $FRUIT!"

done

for ((i = 1; i <= 5; i++)); do
    echo "$i Hello, World!"
done

COUNTER=1

while [ $COUNTER -le 3 ]; do
    echo "Counter is $COUNTER"
    ((COUNTER++))
done

COUNTER=0

until [ $COUNTER -gt 5 ]; do
    echo "Counter is $COUNTER"
    ((COUNTER++))
done

for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo "Hello, World! $i"
done

for i in {1..10}; do
    if [ $i -eq 5 ]; then
        continue
    fi
    echo "using continue Hello, World! $i"
done

# Use while loop to read each line of the file
while IFS= read -r LINE; do
    echo "Line: $LINE"
done < file.txt

# Using while read to get NAME and NUM
while read -r NAME NUM; do
    # echo "Line: $NAME $NUM"
    echo "Name: $NAME, Number: $NUM"
done < file.txt

echo "End of script"
