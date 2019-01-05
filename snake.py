#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 03:53:46 2019

@author: jcarraascootarola
"""
import numpy as np
from random import uniform
import tkinter as tk
import time






class SnakeGame():
    nextMove=None
    
    def __init__(self,xSize,ySize,rendered):
        self.board=Board(xSize,ySize)
        self.snake=Snake([xSize/2,ySize/2])
        self.foodPosition=[int(xSize/2)+10,int(ySize/2)]
        self.score=0
        self.xSize=xSize
        self.ySize=ySize
        self.rendered=rendered
        
        
        if rendered==True:
            self.rectangles=[]
            self.app = tk.Tk()
            self.canvas = tk.Canvas(self.app, width=(self.xSize+2)*10, height=(self.ySize+2)*10)
            
            self.initRender()
    def play(self):
        self.nextMove()
    
    
    def startGame(self):
        self.addFood()
        self.board.update(self.snake.snakeBody,self.foodPosition)
        
        
    def moveForward(self):
        
        self.snake.move()
        self.eaten()
        self.board.update(self.snake.snakeBody,self.foodPosition)
        if self.rendered:
            self.render()
    
    def turnRight(self):
        self.snake.changeDirection(1)
        self.snake.move()
        self.eaten()
        
        self.board.update(self.snake.snakeBody,self.foodPosition)
        if self.rendered:
            self.render()
    
    def turnLeft(self):
        self.snake.changeDirection(-1)
        self.snake.move()
        self.eaten()
        self.board.update(self.snake.snakeBody,self.foodPosition)
        if self.rendered:
            self.render()
       
        
        
    def eaten(self):
        if self.snake.snakeBody[0]==self.foodPosition:
            self.snake.eat()
            self.addFood()
            self.score=self.score+1
        
    def isAlive(self):
       
        if self.snake.snakeBody[0][0]==0 or self.snake.snakeBody[0][0]==self.xSize+1 or self.snake.snakeBody[0][1]==0 or self.snake.snakeBody[0][1]==self.ySize+1:       
            
            return False
        if self.snake.snakeBody[0]  in self.snake.snakeBody[2:]:
            
            return False
        return True
        
    def initRender(self):
        self.app.title("snake")
        
        self.board.update(self.snake.snakeBody,self.foodPosition)
        self.canvas.pack()
        
        colors=["white","green","black","red"]
        for i in range(len(self.board.boardMatrix)):
            self.rectangles.append([])
            
            for j in range(len(self.board.boardMatrix[i])):
                self.rectangles[i].append(self.canvas.create_rectangle(i*10,j*10 , i*10+10, j*10+10, fill=colors[int(self.board.boardMatrix[i][j])], outline = colors[int(self.board.boardMatrix[i][j])]))                 
        
        self.canvas.update()
        
    def render(self):
        colors=["white","green","black","red"]
        for i in range(len(self.board.boardMatrix)):
            for j in range(len(self.board.boardMatrix[i])):
                self.canvas.itemconfig(str(self.rectangles[i][j]),fill=colors[int(self.board.boardMatrix[i][j])], outline = colors[int(self.board.boardMatrix[i][j])])
                
        self.canvas.update()
        
    
    def endGame(self):
        return self.score
    
    def addFood(self):
        
        while(True):
            newPos=[np.random.randint(1,self.xSize),np.random.randint(1,self.ySize)]
            if  newPos not in self.snake.snakeBody :
                break
        self.foodPosition=newPos
        


class Board():
    
    def __init__(self,xSize,ySize):
       self.boardMatrix=np.pad(np.zeros((xSize,ySize)), pad_width=1, mode='constant', constant_values=1)
       self.xSize=xSize
       self.ySize=ySize
       
        
    def renderFood(self,foodPosition):
        
        self.boardMatrix[foodPosition[0]][foodPosition[1]]=-1
        
    
    def cleanBoard(self):
        self.boardMatrix=np.pad(np.zeros((self.xSize,self.ySize)), pad_width=1, mode='constant', constant_values=1)
        
    def renderSnake(self, snakeBody):
        for i in snakeBody:
            
            self.boardMatrix[int(i[0])][int(i[1])]=2
    
    def update(self,snakeBody,foodPosition):
        self.cleanBoard()
        self.renderSnake(snakeBody)
        self.renderFood(foodPosition)
        
       
       
class Snake():
    def __init__(self,position):
        self.snakeBody=[]
        self.snakeBody.append(position)
        self.directions=[[1,0],[0,1],[-1,0],[0,-1]]
        self.changed=0
        self.headDirection=self.directions[0]
        
    def move(self):
        self.snakeBody.insert(0,[self.snakeBody[0][0]+self.headDirection[0],self.snakeBody[0][1]+self.headDirection[1]])
        self.snakeBody.pop()
        
    def eat(self,):
        self.snakeBody
        self.snakeBody.append(self.snakeBody[-1])
        
    def changeDirection(self,direction):
        
        self.changed=self.changed+direction
        self.headDirection=self.directions[self.changed%4]
        
        

    
    

    
    



        
        
    
       