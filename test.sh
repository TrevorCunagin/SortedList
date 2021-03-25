#!/usr/bin/env bash

#Testing normal sort
python3 sort.py < SortMe1.txt > normaloutput.txt
if cmp -s normalsorted.txt normaloutput.txt; then
	echo "First test passed"
else
	echo "First test failed"
fi

#Testing reverse sort
python3 sort.py < SortMe2.txt > reverseoutput.txt
if cmp -s reversesorted.txt reverseoutput.txt; then
	echo "Second test passed"
else
	echo "Second test failed"
fi
