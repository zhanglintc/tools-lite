#!/bin/sh

port=$1

if [ "${port}" == "" ]; then
    echo Port not given
    exit 1
fi

sudo netstat -ntpl | grep ${port} | awk '{print $7}' | awk -F '/' '{print $0}'

