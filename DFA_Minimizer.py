#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 22:50:17 2018

@author: shashi
"""
import pickle
import sys
from DFA_CLASS import DFA
class TABLE:
    def __init__(self):
        self.content = {}
if __name__ == "__main__":
    with open(sys.argv[1],'rb') as inputfile: #input binary file command line argument 1
        dfa = pickle.load(inputfile)
    table = TABLE()
    #First iteration
    for i in range(0,len(dfa.Q)-1):
        x = dfa.Q[i]
        for j in range(i+1,len(dfa.Q)):
            y = dfa.Q[j]
            table.content[(x,y)] = (bool(x in dfa.Final) ^ bool(y in dfa.Final)) * 1
    #consequent iterations
    #find states which come to crossed state on all symbols and set cross to them
    level = 2
    while True:
        flag = False
        for i in range(0,len(dfa.Q)-1):
            x = dfa.Q[i]
            for j in range(i+1,len(dfa.Q)):
                y = dfa.Q[j]
                if table.content[(x,y)] == level - 1:
                    for i1 in range(0,len(dfa.Q)-1):
                        x1 = dfa.Q[i1]
                        for j1 in range(i1+1,len(dfa.Q)):
                            y1 = dfa.Q[j1]
                            for z in dfa.Alphabet:
                                if dfa.Transition[x1][z] == x and dfa.Transition[y1][z] == y:
                                    if table.content[(x1,y1)] == 0:
                                        table.content[(x1,y1)] = level
                                        flag = True
        if flag == False:
            break
        level = level + 1
    #make new dfa 
    mindfa = DFA()
    #making dfa.Q
    already_included = []
    for i in range(0,len(dfa.Q)):
        x = dfa.Q[i]
        if x in already_included:
            continue
        already_included.append(x)
        mindfa.Q.append(x)
        for j in range(i+1,len(dfa.Q)):
            y = dfa.Q[j]
            if table.content[(x,y)] == 0:
                mindfa.Q[-1] = mindfa.Q[-1] + 'combined-with' + y
                already_included.append(y)
    #alphabet will be same
    mindfa.Alphabet = dfa.Alphabet
    #make the transition table
    for x in mindfa.Q:
        temp = x.split('combined-with')[0]
        x = x.replace('combined-with','-')
        mindfa.Transition[x] = {}
        for y in mindfa.Alphabet:
            for z in mindfa.Q:
                if temp in dfa.Q and dfa.Transition[temp][y] in z:
                    z = z.replace('combined-with','-')
                    mindfa.Transition[x][y] = z;
    #starting state
    mindfa.Start = mindfa.Q[0]
    #final state
    for x in mindfa.Q:
        temp = x.split('combined-with')
        for y in temp:
            if y in dfa.Final:
                mindfa.Final.append(x)
                break
    #replacing combined-with with just -
    mindfa.Q = [x.replace('combined-with','-') for x in mindfa.Q]
    mindfa.Start = mindfa.Start.replace('combined-with','-')
    mindfa.Final = [x.replace('combined-with','-') for x in mindfa.Final]
    with open(sys.argv[2],'w') as outputfile:
        outputfile.write('Q = ' + ' '.join(mindfa.Q) + '\n\n')
        outputfile.write('Alphabet = ' + ' '.join(mindfa.Alphabet) + '\n\n')
        outputfile.write('Transition Table =\n\t' + '\t'.join(mindfa.Alphabet) + '\n')
        for x in mindfa.Q:
            outputfile.write(x + '\t')
            for y in mindfa.Alphabet:
                outputfile.write(mindfa.Transition[x][y] + '\t')
            outputfile.write('\n')
        outputfile.write('\n')
        outputfile.write('Start = ' + mindfa.Start + '\n\n')
        outputfile.write('Final = ' + ' '.join(mindfa.Final) + '\n')        