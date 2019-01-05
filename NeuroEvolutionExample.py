#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:33:47 2018

@author: jcarraascootarola
"""

from random import randint
from NeuroEvolution import NeuroEvolution
from NeuralNetwork import NeuralNetwork
from SigmoidNeuron import SigmoidNeuron
import time
import matplotlib.pyplot as plt
import math
from snake import SnakeGame



#hiperparameters
mutationRate = 0.05
populationSize = 100
#datos de la red neuronal initLearningRate  no es usado pero debe ser incializidao para la red neuronal
initLearningRate=0.02
numberOfInputs=3
#las dos siguientes contienen a las hidden layers mas la capa de output
numberOfLayers =3
numberOfNeuronsPerLayer=[20,15,3]

#stopCondition Parameters
maxGenerations=10
maxMovementsSnake=200

def stopCondition(algorithmInstance):          
    
    if algorithmInstance.numberOfGenerations == maxGenerations:
        return True
    return False


def fitnessFunction(individual,final):
    score = 0
    sn=SnakeGame(100,50,final)
    sn.startGame()
    movements=[sn.moveForward,sn.turnRight,sn.turnLeft]
    nn=NeuralNetwork(initLearningRate, numberOfInputs, numberOfLayers, numberOfNeuronsPerLayer)
    gene=0
    #print("----------------------")
    #print(individual)
    for layer in range(len(numberOfNeuronsPerLayer)):
            for neuron in range(0,numberOfNeuronsPerLayer[layer]):
                
                nn.layers[layer].neurons[neuron].bias=individual[gene][1]
                nn.layers[layer].neurons[neuron].weights=individual[gene][0]
                gene=gene+1
    for i in range(0,maxMovementsSnake):
        board=sn.board
        food=sn.foodPosition
        snakeHead=sn.snake.snakeBody[0]
        
        directionPosition=sn.snake.directions.index(sn.snake.headDirection)
        front= [snakeHead[0]+sn.snake.directions[directionPosition][0],snakeHead[1]+sn.snake.directions[directionPosition][1]]    
        right= [snakeHead[0]+sn.snake.directions[(directionPosition+1)%4][0],snakeHead[1]+sn.snake.directions[(directionPosition+1)%4][1]] 
        left= [snakeHead[0]+sn.snake.directions[directionPosition-1][0],snakeHead[1]+sn.snake.directions[directionPosition-1][1]]
        
        
        #nnInput=[board.boardMatrix[int(front[0])][int(front[1])]-4.0/(1+distance(front,food)),board.boardMatrix[int(right[0])][int(right[1])]-4.0/(1+distance(right,food)),board.boardMatrix[int(left[0])][int(left[1])]-4.0/(1+distance(left,food))]   
        
        nnInput=[board.boardMatrix[int(front[0])][int(front[1])]+distance(front,food),board.boardMatrix[int(right[0])][int(right[1])]+distance(right,food),board.boardMatrix[int(left[0])][int(left[1])]+distance(left,food)]           
        
     
        nnInputNormalized=[]
        for i in nnInput:

            nnInputNormalized.append(normalize(min(nnInput),max(nnInput),i))
        
        result=nn.feed(nnInputNormalized)

        movement=movements[result.index(max(result))]

        sn.nextMove=movement
        sn.play()

        if sn.isAlive()==False:
            
                
            break
    
    
    score=sn.score+1/(1+(distance(snakeHead,food)))   
    
    
    return score
   
def normalize(minimo, maximo, value):
    return float((value - minimo)*(1 - 0)) / float((maximo - minimo) + 0)    

def distance(pointA,pointB):
   
    return math.sqrt((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2 )

neuralNetworkParameters=[initLearningRate, numberOfInputs, numberOfLayers, numberOfNeuronsPerLayer]

ne=NeuroEvolution(mutationRate, populationSize, fitnessFunction, stopCondition,neuralNetworkParameters)
ne.startAlgorithm()


plt.figure(1) 
plt.plot(ne.generation, ne.bestFitness)
plt.xlabel('Generation')
plt.ylabel('Fittest individual fitness')
plt.title("Best individual performance")

plt.figure(2) 
plt.plot(ne.generation, ne.averageFitness)
plt.xlabel('Generation')
plt.ylabel('Population average fitness')
plt.title("Average generation performance")
plt.show()

fitnessFunction(ne.best,True)

