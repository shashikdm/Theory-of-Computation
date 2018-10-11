#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 19:10:26 2018

@author: shashi
"""
import os
import pickle #pickle to sae and load binary file
import sys #for command lines
#from DFA_CLASS import DFA #class file for DFA
def leave():
    print("DFA'S ARE NOT EQUIVALENT\n");
    os.system("rm t-e-m-p-*")
    sys.exit();
if __name__ == "__main__":
    os.system("python3 DFA_Minimizer.py "+sys.argv[1]+" t-e-m-p-1.dfa"); #minimize the given dfa's
    os.system("python3 DFA_Minimizer.py "+sys.argv[2]+" t-e-m-p-2.dfa");
    os.system("python3 DFA_Designer.py t-e-m-p-1.dfa t-e-m-p-1") #convert text file to binary
    os.system("python3 DFA_Designer.py t-e-m-p-2.dfa t-e-m-p-2")
    with open('t-e-m-p-1','rb') as inputfile: #input binary file command line argument 1
        dfa1 = pickle.load(inputfile)
    with open('t-e-m-p-2','rb') as inputfile: #input binary file command line argument 1
        dfa2 = pickle.load(inputfile)
    #First check if number of states are equal
    if len(dfa1.Q) != len(dfa2.Q):
        leave()
    #Second check if alphabet is same
    if dfa1.Alphabet != dfa2.Alphabet:
        leave()
    #Third check if number of final states are equal
    if len(dfa1.Final) != len(dfa2.Final):
        leave()
    #Finally check if transition table is equal
    #Stuck here
    print("DFA'S ARE EQUIVALENT\n");
    os.system("rm t-e-m-p-*")
                