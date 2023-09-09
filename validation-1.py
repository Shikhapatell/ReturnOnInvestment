#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:44:09 2022

@author: shikhapatel
"""

class ValidationClass: 
    
    #checkFloat(self, str_input) – takes a value as a parameter (str_input), and validates that the parameter is a float
    def checkFloat(self, str_input): 
        valid = True
        try: 
            # check if the user has entered valid inputs for initial and current values
            str_input = float(str_input)
            valid = True
            return str_input
        
        except ValueError: 
            valid = False
        
        #only return boolean if it is false
        finally:
            if valid == False:
                return False