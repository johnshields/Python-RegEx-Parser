#!/bin/bash

# tests for a true match
python regex_parser
python regex_parser < "a.b.c"
python regex_parser < "abc"

for match in $(<output)
do
    echo "True"
    echo "$match"
done

# tests for a false match
python regex_parser < "(a.(b|d))*"
python regex_parser < "abc"

for no_match in $(<output)
do
    echo "False"
    echo "$no_match"
done