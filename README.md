# G00348436_gt
# G00348436 - John Shields

ReadMe for Graph Theory Project

# Project Statement
You must write a program in the Python programming language that can build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.

# clone from github
In cmd file directory $ git clone https://github.com/johnshields/G00348436_gt

# Regular Expressions
A regular expression is a string containing a series of characters, some of which may have a special meaning. For example, the three characters ., |, and * have the special meanings concatenate, or, and Kleene star respectively. For example, the regular expression 0.1 means a 0 followed by a 1, 0|1 means a 0 or a 1, and 1* means any number of 1’s. These special characters must be used in your submission.

When you want to perform string matching operations that are more complex than the operations, you use regular expressions.

# Special Characters

., |, *, +, ?, (), $

. concatenates two characters. So, a.b means an a followed by a b

| means or. So, a|b means an a or a b

* (Kleene Star) means a character appears 0 or more times

+ means a character appears 1 or more times

? means a character appears 0 or 1 time

() are used to group characters

$ means a character that does not appear

# Shunting Yard Algorithm

The Shunting Yard Algorithm, created by Edsger Dijkstra converts an Infix Expression to a Postfix Expression using a stack which holds operators. The stack is used to reverse the order of the operators in the expression. Since no operator can be printed until both of its operands have appeared, it also serves as a storage structure.

Takes regular expressions from infix notation to postfix notation

Concatenates operations
Infix:
a.b = a followed by b
a|b = a or b
a* = any number of a's (including 0's)

Postfix:
ab. = a followed by b
ab| = an or b
a* = any number of a's (including 0's)

E.g. - (a|b).(a*|b*) becomes ab|a*b*|

set up a specials dictionary:
specials = {'*': 50, '.': 40, '|': 30, '+':40, '?':35}

set up a for loop to search for the Special Characters
- looks for c in specials dictionary, if not found, give value 0
- looks for top of stack in specials dictionary,  if not found, give value 0

put statements together

# Thompson's Construction

Thompson's Construction, by Ken Thompson, is used to convert a Postfix Expression into a Non-deterministic Finite Automata. These NFAs can be used to match strings against Regular Expressions. 

- reads Regular Expressions from left to right to create nfa's

An NFA is represented by its initial and accepts states
set up classes

In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")

Algorithm:
A function has a stack of NFAs, the pofix allows to loop one character at a time until the regular expression is complete.

The stack works as last in first out
1. pop 2 NFAs off the stack.
2. merges them together
3. Connect 1st NFAs accept state to the 2nd's initial
4. Push NFA to stack
5. Push newnfa 
6. Create new initial and accept states
7. Creates new nfa
8. Join the initial states to the accept state using an arrow labelled c.
8. Going to create a new instance of the NFA class.
9. Set it's initial state to the initial state
10. Push new NFA to the stack # ¬ returns an instance of the nfa class
11. push nfa
# nfastack should only have a single nfa on it at the point.  


# Following e arrows

1. Return the set of states that can be reached from state following e arrows
2. Check if state has arrows labeled e from it
3. Check if edge1 is a state
4. If theres an edge1, follow it
5. Check if edge2 is a state
6. If theres an edge2, follow it
7. Return the set of states

# Matching Regular Expressions

####
'current' = THE CURRENT SET
'upcomin' = THE NEXT SET UPCOMING
####

Shunt and compile the regular expression from the funtions in code
1. Call the shunt and compiletom function
- Current set of states and the next set of the states
2. Add the initial state to the current set
3. Loop through each character in the string
4. Check of that state is labelled s
5. Add edge1 state to the upcomin set
6. Set current to upcomin, and clear out next
7. Check if the accept state is in the set of current states

# Testing the code 

# Testing the Shunting Yard Algorithm
Testing the Shunting Yard Algorithm to see if actually takes a Regular Expression from infix notion to postfix notation.

regex e.g. = (a.b)|(c*.d)

# Print the calling of the fuction 'shunt'
print(shunt("(a.b)|(c*.d)"))

Output:
(a.b)|(c*.d) to ab.c*d.|

# Testing Thompson's Construction

Test to see if the compiletom function can actually make a regex into a NFA.

# Print the calling of the fuction 'compiletom'
print(compiletom("ab.cd.|"))

Output:
<__main__.nfa object at 0x0000028BACDB97F0>

# Testing Matching Regular Expressions
1. Create list of infix regex + Strings to match against the regex infixes.
infixes = ["a.b.c" ,"a.b.c*, a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]

2. Double for loop. For loops through the regex and strings.
strings = ["abc", "abbc", "abcc", "abad", "abbbc"]

3. The match function prints out True/False if the infix regex matches the string.

infix = a.b.c
string = abc

# Print the calling of the function 'match'
print(match(exp, res), exp, res)

Output:
True a.b.c abc
# This tells that this regex infix matches with this string

# Prompt for tests to match Regular Expressions

Type in any Infix and string to be matched and tested

infix = (a.(b|d))* 
string = abc

while loop prints out True/False if the infix regex matches the string

# Function prints out True/False if the infix regex matches the string
print(match(infixes, string), infixes, string)

Output: 
False (a.(b|d))* abc
# This tells that this regex infix does not match with this string

####
crtl+c and then press the 'Enter' key to exit prompt
####

# Problems I had
Besides the typical errors of misspelling and missing :, ), etc. I had one problem that stopped my progress with the project. When the match function was called all the matches would come out as 'False' and 'None'. After attempting to find errors that are not clearly and do not cause the code to crash I tracked it down to my indentation in the for loop in the match function. After I fixed the indentation the output displayed both 'False' and 'True'.

# links:
https://jakevdp.github.io/WhirlwindTourOfPython/14-strings-and-regular-expressions.html
https://docs.python.org/3.3/howto/regex.html
https://www.tutorialspoint.com/python/python_reg_expressions.htm
https://swtch.com/~rsc/regexp/regexp1.html
https://www.youtube.com/watch?v=paOPoZyjzdg
https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html
https://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm
http://www.martinbroadhurst.com/shunting-yard-algorithm-in-python.html
https://swtch.com/~rsc/regexp/regexp1.html
http://www.oxfordmathcenter.com/drupal7/node/628
https://en.wikipedia.org/wiki/Thompson%27s_construction
https://www.youtube.com/watch?reload=9&v=RYNN-tb9WxI
https://www.w3schools.com/python/python_functions.asp

# References for code
# Functions
# https://www.w3schools.com/python/python_functions.asp
# Shunting Yard Algorithm
# https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html
# https://web.microsoftstream.com/video/cfc9f4a2-d34f-4cde-afba-063797493a90
# http://www.martinbroadhurst.com/shunting-yard-algorithm-in-python.html
# Thompson's Construction
# https://web.microsoftstream.com/video/5e2a482a-b1c9-48a3-b183-19eb8362abc9
# https://xysun.github.io/posts/regex-parsing-thompsons-algorithm.html
# Matching
# https://web.microsoftstream.com/video/6b4ba6a4-01b7-4bde-8f85-b4b96abc902a
# Prompt
# https://stackoverflow.com/questions/70797/user-input-and-command-line-arguments
# https://stackabuse.com/getting-user-input-in-python/
# https://stackoverflow.com/questions/3754620/a-basic-question-about-while-true
