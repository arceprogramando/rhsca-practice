#!/bin/bash

function show_usage {
    echo "Usage: $0 source_dir dest_dir"
    if [ $# -eq 0 ]; then
        exit 99 # Exit with arbitrary nonzero return code
    else
        exit 1
    fi
}

# Main program start here

if [ $# -ne 2 ]; then
    show_usage
else # There are two arguments
    if [ -d "$1" ]; then
        source_dir=$1
    else
        echo 'Invalid source directory'
        show_usage
    fi 

    if [ -d "$2" ]; then
        dest_dir=$2
    else
        echo 'Invalid destination directory'
        show_usage
    fi
fi

printf "Source directory is ${source_dir}\n"
printf "Destination directory is ${dest_dir}\n"


