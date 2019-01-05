#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:45:51 2018

@author: jcarraascootarola
"""
from random import randint
from random import random
from random import uniform
from statistics import mean 
import numpy as np

class NeuroEvolution:

    population =[]
    popFitness =[]
    bestFitness = []
    averageFitness = []
    generation = []
    best = None
    numberOfGenerations = 0
    
    def __init__(self,mutationRate, populationSize, fitnessFunction, stopCondition,neuralNetworkInit):
        self.mutationRate = mutationRate
        self.populationSize = populationSize
        self.fitnessFunction = fitnessFunction
        self.stopCondition = stopCondition
        #k is the tournament selection size
        self.k = int(2*populationSize)
        self.geneValues=[-2,2]
        self.neuralNetworkInit=neuralNetworkInit

        
    def startAlgorithm(self):
        self.popCreation()
        while True:
            
            self.generation.append(self.numberOfGenerations)
            self.evaluateFitness()
            self.bestFitness.append(max(self.popFitness))
            
            if self.best == None or self.bestFitness[-1] > self.fitnessFunction(self.best,False):
                self.best = self.population[self.popFitness.index(max(self.popFitness))]
            
            if self.stopCondition(self):
                break
            self.reproduction()
            self.numberOfGenerations+=1
      
    def popCreation(self):
        for i in range(self.populationSize):
            self.population.append(self.neuralNetworkCreation())
       
    
    #neuralNetworkInit = initLearningRate, numberOfInputs, numberOfLayers, numberOfNeuronsPerLayer 
    def neuralNetworkCreation(self):
        network=[]
        newLayerNeuronCount=[self.neuralNetworkInit[1]]+ self.neuralNetworkInit[3]
        for i in range(self.neuralNetworkInit[2]):
            for j in range(newLayerNeuronCount[i+1]):
                neuron = []
                neuron.append(np.random.uniform(-2.0,2.0,newLayerNeuronCount[i]))
                neuron.append(uniform(-2.0, 2.0))
                network.append(neuron)
              
        
        return network
    
            
    def evaluateFitness(self):
        self.popFitness = []
        for i in range(self.populationSize):
           
            self.popFitness.append(self.fitnessFunction(self.population[i],False))
        self.averageFitness.append(mean(self.popFitness))
            
    def selection(self):
        best = None
        bestIndex = 0
        
        for i in range(self.k):
            index = randint(0, self.populationSize-1)
            if best == None or self.popFitness[index] > self.popFitness[bestIndex]:
                best = self.population[index]
                bestIndex = index
                
        
        return best
    
    def reproduction(self):
        newPopulation = []
        for i in range(self.populationSize):
            
            parent1 = self.selection()
            parent2 = self.selection()
            
            baby = self.crossOver(parent1,parent2)
            baby = self.mutate(baby)
            score=self.fitnessFunction(baby,False)
            
           
            newPopulation.append(baby)
        self.population = newPopulation
            
    def crossOver(self,parent1 ,parent2):

        
        mixingPoint = randint(0, len(parent1))
        baby =[]
        for i in range(mixingPoint):
            baby.append(parent1[i])
        for i in range(mixingPoint,len(parent1)):
            baby.append(parent2[i])
        
        return baby
        
    def mutate(self,individual):
        mutatedIndividual=individual
        for i in range(len(individual)):
            if random() < self.mutationRate:
                newNeuron=mutatedIndividual[i]
                newNeuron[0]=np.random.uniform(-2.0,2.0,len(newNeuron[0]))
                newNeuron[1]=uniform(-2.0, 2.0)
                mutatedIndividual[i] = newNeuron
        return mutatedIndividual