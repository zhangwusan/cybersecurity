#!/bin/bash

# Check even number
isEvenNumber() {
    if [ $(( $1 % 2 )) -eq 0 ]; then
        return 0
    else
        return 1
    fi
}

NUMBER=22
isEvenNumber $NUMBER
if [ $? -eq 0 ]; then
    echo "The number $NUMBER is even."
else
    echo "The number $NUMBER is odd."
fi


sum() {
    local sum=0
    for num in "$@"; do
        (( sum += num ))
    done
    echo $sum
}

numbers=(1 2 3 4 5)
echo "The sum of the numbers in the array is $(sum "${numbers[@]}")."