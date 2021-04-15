#!/usr/bin/env bash

#Testing normal sort
python3 sort.py < SortMe.txt > normaloutput.txt
if diff normalsorted.txt normaloutput.txt; then
	echo "First test passed"
else
	echo "First test failed"
fi

#Testing reverse sort
python3 sort.py < SortMe.txt > reverseoutput.txt
if diff reversesorted.txt reverseoutput.txt; then
	echo "Second test passed"
else
	echo "Second test failed"
fi
