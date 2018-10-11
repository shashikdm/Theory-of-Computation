#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 22:30:50 2018

@author: shashi
"""
import pickle #pickle to sae and load binary file
import sys #for command lines
from DFA_CLASS import DFA #class file for DFA


def check_syntax(line, length, string):
    if inputstring[line][0:length] != string: #checking for syntax
        print("SYNTAX ERROR IN LINE "+str(line+1)+"\n")
        sys.exit()


if __name__ == "__main__":
    if sys.argv[1][-4:] != '.dfa':
        print("UNEXPECTED INPUT FILE FORMAT\n")
        sys.exit()
    dfa = DFA() #creates an object of class DFA
    inputfile = open(sys.argv[1], 'r') #opens input text file give first command line argument
    inputstring = inputfile.read().split('\n\n'); #splits the tuple
    check_syntax(0,4,"Q = ") #checking for syntax
    try:
        dfa.Q = inputstring[0][4:].split() #No. of states checking if integer
    except:
        print("SYNTAX ERROR IN LINE 1\n")
        sys.exit()
    check_syntax(1,11,"Alphabet = ")
    try:
        dfa.Alphabet = inputstring[1][11:].split() #Alphabets
    except:
        print("SYNTAX ERROR IN LINE 2\n")
        sys.exit()
    check_syntax(2,19,"Transition Table =\n")
    try:
        dfa.Transition = {} #construction of transition table
        inputstring[2] = inputstring[2][19:].split('\n')
        inputstring[2][0] = inputstring[2][0].split('\t')
        for i in range(1, len(dfa.Q)+1):
            inputstring[2][i] = inputstring[2][i].split('\t')
            transition = {}
            j = 1;
            for x in inputstring[2][0][1:]:
                transition[x] = inputstring[2][i][j]
                j = j + 1
            dfa.Transition[inputstring[2][i][0]] = transition
    except:
        print("SYNTAX ERROR IN TRANSITION TABLE\n")
        sys.exit()
    check_syntax(3,8,"Start = ")
    try:
        dfa.Start = inputstring[3][8:] #start state
        if dfa.Start not in dfa.Q:
            raise Exception()
    except:
        print("SYNTAX ERROR IN LINE 4\n")
        sys.exit()
    check_syntax(4,8,"Final = ")
    try:
        dfa.Final = inputstring[4][8:].split() #final states
    except:
        print("SYNTAX ERROR IN LINE 5\n")
        sys.exit()
    with open(sys.argv[2],'wb') as outputfile: #store it in binary file command line argument #2
        pickle.dump(dfa,outputfile)
