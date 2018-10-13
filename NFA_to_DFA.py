#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:13:01 2018

@author: shashi
"""
import pickle #pickle to sae and load binary file
import sys #for command lines
from DFA_CLASS import DFA as NFA #class file for DFA
from DFA_CLASS import DFA
from collections import Counter

def check_syntax(line, length, string):
    if inputstring[line][0:length] != string: #checking for syntax
        print("SYNTAX ERROR IN LINE "+str(line+1)+"\n")
        sys.exit()


if __name__ == "__main__":
    if sys.argv[1][-4:] != '.nfa':
        print("UNEXPECTED INPUT FILE FORMAT\n")
        sys.exit()
    nfa = NFA() #creates an object of class nfa
    inputfile = open(sys.argv[1], 'r') #opens input text file give first command line argument
    inputstring = inputfile.read().split('\n\n'); #splits the tuple
    check_syntax(0,4,"Q = ") #checking for syntax
    try:
        nfa.Q = inputstring[0][4:].split() #No. of states checking if integer
    except:
        print("SYNTAX ERROR IN LINE 1\n")
        sys.exit()
    check_syntax(1,11,"Alphabet = ")
    try:
        nfa.Alphabet = inputstring[1][11:].split() #Alphabets
    except:
        print("SYNTAX ERROR IN LINE 2\n")
        sys.exit()
    check_syntax(2,19,"Transition Table =\n")
    try:
        nfa.Transition = {} #construction of transition table
        inputstring[2] = inputstring[2][19:].split('\n')
        inputstring[2][0] = inputstring[2][0].split('\t')
        for i in range(1, len(nfa.Q)+1):
            inputstring[2][i] = inputstring[2][i].split('\t')
            transition = {}
            j = 1;
            for x in inputstring[2][0][1:]:
                transition[x] = inputstring[2][i][j]
                j = j + 1
            nfa.Transition[inputstring[2][i][0]] = transition
    except:
        print("SYNTAX ERROR IN TRANSITION TABLE\n")
        sys.exit()
    check_syntax(3,8,"Start = ")
    try:
        nfa.Start = inputstring[3][8:] #start state
        if nfa.Start not in nfa.Q:
            raise Exception()
    except:
        print("SYNTAX ERROR IN LINE 4\n")
        sys.exit()
    check_syntax(4,8,"Final = ")
    try:
        nfa.Final = inputstring[4][8:].split() #final states
    except:
        print("SYNTAX ERROR IN LINE 5\n")
        sys.exit()
    #Lazy evaluation starts here
    dfa = DFA()
    dfa.Start = '{' + nfa.Start + '}'
    dfa.Q.append(dfa.Start)
    dfa.Alphabet = nfa.Alphabet;
    while True:
        finished = True
        for x in dfa.Q:
            if dfa.Transition.get(x) == None:
               finished = False
               current_state = x[1:-1].split('-')
               dfa.Transition['{'+'-'.join(current_state)+'}'] = {}
               break
        if finished == True:
            break;
        for y in nfa.Alphabet:
            new_state = ''
            for x in current_state:
                transition = ''
                for z in nfa.Transition[x][y].split():
                    if z not in new_state:
                        if transition == '':
                            transition = z
                        else:
                            transition = transition + '-' +z 
                if new_state != '' and transition != '':
                    new_state = new_state +'-'+ transition
                elif transition!='':
                    new_state = transition
            new_state = new_state.split('-')
            new_state.sort()
            new_state = '-'.join(new_state)
            if new_state not in [y[1:-1] for y in dfa.Q]:
                dfa.Q.append('{'+new_state+'}')
            dfa.Transition['{'+'-'.join(current_state)+'}'][y] = '{'+new_state+'}'
    for x in dfa.Q:
        for y in nfa.Final:
            if y in x:
                dfa.Final.append(x)
    #write into a file
    with open(sys.argv[2],'w') as outputfile:
        outputfile.write('Q = ' + ' '.join(dfa.Q) + '\n\n')
        outputfile.write('Alphabet = ' + ' '.join(dfa.Alphabet) + '\n\n')
        outputfile.write('Transition Table =\n\t' + '\t'.join(dfa.Alphabet) + '\n')
        for x in dfa.Q:
            outputfile.write(x)
            for y in dfa.Alphabet:
                outputfile.write('\t'+dfa.Transition[x][y])
            outputfile.write('\n')
        outputfile.write('\n')
        outputfile.write('Start = ' + dfa.Start + '\n\n')
        outputfile.write('Final = ' + ' '.join(dfa.Final) + '\n')
            