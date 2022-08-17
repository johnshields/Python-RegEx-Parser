#!/bin/bash
python3 regex_parser.py
# tests for a false match
cat < output.txt | while read -r match
do
    echo "no match: $match" | tee false.txt
done
