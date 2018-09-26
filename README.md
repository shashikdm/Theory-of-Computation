# Theory-of-Coputation
This repository contains various programs related to the theory of computation

requirements:
python3, pickle library

first commit: dfa, human readable text to class file (DFA_Designer) and testing strings ((DFA_Tester)
<text file in valid syntax> -> DFA_Designer -> binary file -> DFA_Tester -> String(ACCEPT/REFECT)

How to run?
edit the 'input.txt' file in following syntax
first row: number of states
leave one row empty
next row: space seperated alphabets
leave one row empty
next row: one tab and then tab seperated alphabets
next rows: state number, tab and then tab seperated transition states
leave one row empty
next row: starting state
leave one row empty
next row: final states

Then execute DFA_Designer followed by DFA_Tester
