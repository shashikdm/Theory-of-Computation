#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 23:17:39 2018

@author: shashi
"""
class DFA:
    def __init__(self):
        self.Q = []
        self.Alphabet = []
        self.Transition = {}
        self.Start = ''
        self.Final = []
        
