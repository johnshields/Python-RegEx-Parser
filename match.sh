#!/bin/bash
python3 regex_parser.py
# tests for a true match
cat < output.txt | while read -r match
do
    echo "match: $match" | tee true.txt
done
