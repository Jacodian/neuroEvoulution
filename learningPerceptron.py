#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:21:00 2018

@author: jcarraascootarola
"""

import numpy as np
import random

class LearningPerceptron:

    
    def __init__(self, initLearningRate,numberOfInputs):
        self.bias = random.uniform(-2.0, 2.0)
        self.learningRate=initLearningRate
        self.weights=np.random.uniform(-2.0,2.0,numberOfInputs)
           
        
    def activate(self, inputData):
             
        return int(sum(self.weights * np.array(inputData)) + self.bias > 0)
    
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
    
        