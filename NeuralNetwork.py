#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 03:45:50 2018

@author: jcarraascootarola
"""

from SigmoidNeuron import SigmoidNeuron 
import numpy as np






class NeuronLayer:

    def __init__(self, learningRate, numberOfNeurons, numberOfInputs):
        self.neurons=[]
        self.lastOutputs=[]
        for i in range(numberOfNeurons):
            self.neurons.append(SigmoidNeuron(learningRate, numberOfInputs))
            self.lastOutputs.append(0)
        
    
    def feed(self, inputs):

        for i in range(len(self.neurons)):
            self.lastOutputs[i]=self.neurons[i].activate(inputs)
       
        return self.lastOutputs
    
    def backPropagation(self, errors):
        errorsArray = np.array(errors)
        unos =np.ones(len(self.lastOutputs))
        delta=errorsArray*self.lastOutputs*(unos-self.lastOutputs)
        
        newError=np.zeros(len(self.neurons[0].weights))

        for i in range(len(self.neurons)):
            newError=newError+self.neurons[i].weights*delta[i]
 
        return [newError,delta]
    
    def updateWeights(self,delta,inputs):
        inputsArray=np.array(inputs)
        for i in range(len(self.neurons)):
            self.neurons[i].weights=self.neurons[i].weights+self.neurons[i].learningRate*delta[i]*inputsArray
            self.neurons[i].bias=self.neurons[i].bias+self.neurons[i].learningRate*delta[i]
        



class NeuralNetwork:

    
    def __init__(self, initLearningRate, numberOfInputs, numberOfLayers, numberOfNeuronsPerLayer):
        self.layers=[]
        inputsPerLayer = [numberOfInputs] + numberOfNeuronsPerLayer
        for i in range(numberOfLayers):          
            self.layers.append(NeuronLayer(initLearningRate , numberOfNeuronsPerLayer[i],inputsPerLayer[i]))
        
        
        
    def feed (self,inputs):
        outputs=inputs
        for i in range(len(self.layers)):
            outputs=self.layers[i].feed(outputs)
            
        return outputs
    

    def train(self, inputs , expectedOutputs):
        
       
        
        for i in range(len(inputs)):
            deltas=[]
            outputs=np.array(self.feed(inputs[i]))


            error =np.array(expectedOutputs[i])-outputs
            for j in range(len(self.layers)):
                layerActual=self.layers[-(1+j)]
                [error,delta]=layerActual.backPropagation(error)
                
                deltas.insert(0,delta)

            auxInputs=inputs[i]
            for j in range(len(self.layers)):
                   
                self.layers[j].updateWeights(deltas[j],auxInputs)
                auxInputs=self.layers[j].feed(auxInputs)
        
    def epochTrainingPrediction(self,trainSet,validationSet,numberOfEpochs):
        trainingResults=[[],[]]
        for i in range(numberOfEpochs):
            
            self.train(trainSet[0],trainSet[1])
            total=len(validationSet[0])
            rights=0
            
            for j in range(total):
                result=self.feed(validationSet[0][j])
                
                indiceMaximo=result.index(max(result))
                
                if validationSet[1][j][indiceMaximo]==1:
                    rights=rights+1
                   
            trainingResults[0].append(i)  
            trainingResults[1].append(float(rights)/total)
        print(self.layers[-1].neurons[0].weights)
        print(self.layers[-1].neurons[1].weights)
        return(trainingResults)
            
    
        






