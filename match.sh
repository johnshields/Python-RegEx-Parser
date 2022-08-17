#!/bin/bash
python3 regex_parser.py
# tests for a true match
cat < bash_tests/output.txt | while read -r match
do
    echo "match: $match" | tee bash_tests/true.txt
done
