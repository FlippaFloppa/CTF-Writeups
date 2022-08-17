#!/bin/bash



for i in {162..0}; do
res=$(./mocr.py pwd.png | tr -d '\n')
unzip -o -j -P $res "flag_$i.zip"
done
