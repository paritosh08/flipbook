#!/bin/bash
flipLoc=$1
flag=$2
outF=$3
if [ -z "$flipLoc" ]; then
	echo Wrong arguments
else
	if [ -z "$flag" ]; then
		echo Wrong arguments
	else
		if [ -z "$outF" ]; then
			echo Wrong arguments
		else
			if [ $flag=="-o" ; then
				if ! command -v python
				then
					if ! command -v python3
					then
						echo Please check if python3 is installed
					else
						python3 code.py $1 $3
						echo Done
					fi
				else
					python code.py $1 $3
					echo Done
				fi
			else
				echo Wrong arguments
			fi
		fi
	fi
fi