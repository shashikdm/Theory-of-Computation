#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 23:32:07 2018

@author: shashi
"""
import pickle
with open('binary','rb') as inputfile:
    dfa = pickle.load(inputfile)
while True:
    test = input('ENTER THE STRING\n')
    state = dfa.Start
    for a in test:
        state = dfa.Transition[state][a]
    if state in dfa.Final:
        print('ACCEPTED')
    else:
        print('REJECTED')
    choice = input('DO YOU WANT TO CONTINUE?(y/n)')
    if choice == 'y':
        continue
    else:
        break
        
