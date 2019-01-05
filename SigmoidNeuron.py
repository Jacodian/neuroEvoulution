#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:22:58 2018

@author: jcarraascootarola
"""

import numpy as np
import random

class SigmoidNeuron:
    
    
    def __init__(self, initLearningRate,numberOfInputs):
        self.lastOutput=0
        self.bias = random.uniform(-2.0, 2.0)
        self.learningRate=initLearningRate
        self.weights=np.random.uniform(-2.0,2.0,numberOfInputs)
           
            
    def activate(self, inputData):    
        self.lastOutput = 1.0/(1+np.exp(-(sum(self.weights * np.array(inputData)) + self.bias)))
        return self.lastOutput
    
    def train(self,trainingSet,expectedValues):
        
        for trainingInput,exVal in trainingSet,expectedValues:
            result=self.activate(trainingInput)
            if result != exVal:
                self.learn(result,exVal,trainingInput)
        
    def learn(self,realOutput, expectedOutput,inputN):
        diff= realOutput-expectedOutput
        for i in range(len(self.weights)):
            self.weights[i]= self.weights[i] + (self.learningRate*inputN*diff)
        
        self.bias=self.bias +(self.learningRate*diff)