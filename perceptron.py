#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 20:44:42 2018

@author: jcarraascootarola
"""
import numpy as np

class Perceptron:

    
    bias = 10
    weights = np.array([1,1])
    

    
    def __init__(self, initWeights, initThreshold):
        self.bias = initThreshold
        self.weights = np.array(initWeights)
        
    def activate(self, inputData):
        
        return int(sum(self.weights * np.array(inputData)) + self.bias > 0)
    

class NandPerceptron(Perceptron):
    
    bias = 3
    weights = np.array([-2,-2])
    def __init__(self):
        pass


class AndPerceptron(Perceptron):
    
    bias = -1
    weights = np.array([1,1])
    def __init__(self):
        pass


class OrPerceptron(Perceptron):
    
    bias = 0
    weights = np.array([1,1])
    def __init__(self):
        pass
    

class SumGate:
    topPerceptron=NandPerceptron()
    botPerceptron=NandPerceptron()
    midPerceptron=NandPerceptron()
    carryPerceptron=NandPerceptron()
    outputPerceptron=NandPerceptron()
    def __init__(self):
        pass
    
    def add(self,x1,x2):
        midResult=self.midPerceptron.activate([x1,x2])
        topResult=self.midPerceptron.activate([x1,midResult])
        botResult=self.midPerceptron.activate([midResult,x2])
        
        return [self.outputPerceptron.activate([topResult,botResult]),self.carryPerceptron.activate([midResult,midResult])]
    



a= SumGate()

print(a.add(0,0))