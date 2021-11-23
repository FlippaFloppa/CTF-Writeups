#!/bin/bash

for i in {1..1000}
do
    error=$(./bof $(python -c "print('A'*$i)") 2>&1 1>tmp.txt); exit=$?;
    if [ $exit -ne 0 ]
    then 
        echo Va in overflow da $i; break;
    fi
done