#!/bin/bash

readonly INT=6h
if [ "$1" == '-url' ]; then
    while [ true ]
    do

    python3 main.py $2

    sleep $INT

    done
else
    echo "Oh....Enter url"
fi