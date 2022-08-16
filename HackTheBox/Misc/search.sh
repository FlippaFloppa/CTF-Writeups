#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage: ./search.sh /path/to/.secret"
    exit 1
fi

for i in $(find $1); do
       res=`echo -n $i | cut -d/ -f3`
       if [[ ! -z "$res" ]]
       then echo $res $i
       fi
done | sort -n | cut -d/ -f2 | tr -d ' ','.','\n' | base64 -d