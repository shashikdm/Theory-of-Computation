#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 23:32:07 2018

@author: shashi
"""
import pickle
import sys
#from DFA_CLASS import DFA
if __name__ == "__main__":
    with open(sys.argv[1],'rb') as inputfile: #input binary file command line argument 1
        dfa = pickle.load(inputfile)
    while True: #test as long as user wants
        test = input('ENTER THE STRING\n')
        state = dfa.Start
        for a in test: #loop over all the symbols in the test string
            state = dfa.Transition[state][a]
        if state in dfa.Final: #check if last state is a final state
            print('ACCEPTED')
        else:
            print('REJECTED')
        choice = input('DO YOU WANT TO CONTINUE?(y/n): ') #ask user whether to continue or not
        if choice == 'y':
            continue
        else:
            break
        
