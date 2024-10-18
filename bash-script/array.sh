#!/bin/bash

fruits=("apple" "banana" "cherry")
echo "${fruits[@]}"

subfruits=("${fruits[@]:1:2}")
echo "${subfruits[@]}"



declare -A colors
colors=( ["apple"]="red" ["banana"]="yellow" ["cherry"]="green")
echo "${!colors[@]}"
echo "${colors["apple"]}"