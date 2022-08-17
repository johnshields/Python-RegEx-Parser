#!/bin/bash
python3 regex_parser.py
# tests for a false match
cat < bash_tests/output.txt | while read -r match
do
    echo "no match: $match" | tee bash_tests/false.txt
done
