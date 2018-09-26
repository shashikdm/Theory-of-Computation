#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 22:30:50 2018

@author: shashi
"""
#class defination for a DFA
import pickle
class DFA:
    def __init__(self):
        self.Q = int(inputstring[0])
        self.Alphabet = inputstring[1].split()
        self.Transition = []
        inputstring[2] = inputstring[2].split('\n')
        inputstring[2][0] = inputstring[2][0].split('\t')
        for i in range(1, self.Q+1):
            inputstring[2][i] = inputstring[2][i].split('\t')
            transition = {}
            j = 1;
            for x in inputstring[2][0][1:]:
                transition[x] = int(inputstring[2][i][j])
                j = j + 1
            self.Transition.append(transition)
        self.Start = int(inputstring[3])
        self.Final = [int(x) for x in inputstring[4].split()];

inputfile = open('input.txt', 'r')
inputstring = inputfile.read().split('\n\n');
dfa = DFA()
with open('binary','wb') as outputfile:
    pickle.dump(dfa,outputfile)
