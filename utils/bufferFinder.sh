#!/bin/bash

if [ $# -ne 1 ]
then
	echo Usage: ./buff2.sh nomefile
	exit
fi

for i in {1..4096}
do
	#to speed up i do it every 32 bytes
	if [ `expr $i % 32` -eq 0 ]
	then
		echo provo con $i
		error=$($1 $(python -c "print('A'*$i)") 2>&1 1>tmp.txt); exit=$?;
		if [ $exit -ne 0 ]
		then 
			echo Va in overflow da $i
			num=`expr $i - 32`
			for j in $(seq $num $i)
			do	
				echo provo con $j
				error=$($1 $(python -c "print('A'*$j)") 2>&1 1>tmp.txt); exit=$?;
				if [ $exit -ne 0 ]
				then
					echo Va in overflow da $j; exit;
				fi
			done
		fi
	fi
done
