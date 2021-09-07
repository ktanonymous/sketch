#!/bin/bash

containername=$(eval echo '$'$#)

if [ -z "$containername" ]; then
    echo "Must pass 'python' or 'db' to this script."
    exit 1
fi

if [ "$containername" != "python" -a "$containername" != "db" ]; then
    echo "argument must be 'python' or 'db'."
    exit 2
fi

docker exec -it "$containername" /bin/bash
