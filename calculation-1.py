#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 17:00:10 2022

@author: shikhapatel
"""

class CalculationClass: 
    
    #Three attributes:__initialValue, __currentValue, __ROI 
    def __init__(self, initialValue, currentValue): 
        self.__initialValue = initialValue 
        self.__currentValue = currentValue
        
         
        
    # Contains at least one method: calcROI(self) which calculates the ROI.
    def calcROI(self): 
        netValue = self.__currentValue - self.__initialValue
        ROI = netValue / self.__initialValue
        self.__ROI = ROI * 100
        
        #returns the ROI value
        return self.__ROI 
    
    
    
    