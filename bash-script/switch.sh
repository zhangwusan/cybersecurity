#!/bin/bash

# case variable in 
#     pattern1)
#         # command line
#     ;;
#     pattern2)
#         # command line
#     ;;
#     *)
#         # command line
#     ;;

# esac

FRUIT="apple"

case $FRUIT in
    apple)
        echo "I love apples."
        ;;
    banana)
        echo "I hate bananas."
        ;;
    *)
        echo "I don't know this fruit."
        ;;
esac