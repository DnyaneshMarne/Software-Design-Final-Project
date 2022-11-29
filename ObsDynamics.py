from tkinter import *
from PIL import Image
import random
import os
from abc import ABC,abstractmethod
from ObstacleFactory import Factory
from queue import PriorityQueue



class ObsDynamics():

    def __init__(self,Gamew):

        self.facObj = Factory()
        self.ghost = self.facObj.create("Ghost",550,random.randint(100, 300))
        self.castle1 = self.facObj.create("Castle1",550,random.randint(600, 600))
        self.castle2 = self.facObj.create("Castle2",550,random.randint(600, 600))
        self.house = self.facObj.create("House",550,random.randint(600, 600))
        self.tree = self.facObj.create("Tree",550,random.randint(600, 600))
        self.pumpkin = self.facObj.create("Pumpkin",650,670) 
        self.obs_pool = [self.castle1, self.castle2, self.tree,self.house,self.pumpkin]
        self.gw = Gamew
        self.score = 0
        self.priorityObstacle = PriorityQueue()
        self.priorityObstacle.put((self.ghost.x,self.ghost.y,self.ghost))
        self.sWin = self.gw.getCanvas().create_text(15, 45, text="0", font='Impact 60', fill='#ffffff', anchor=W)
        random.seed(10)


    def get_rand_obs(self):

        self.obs_obj = self.obs_pool[random.randint(0,3)]
        self.cloned_obj = self.facObj.clone(self.obs_obj)
        self.pump_obj =self.facObj.clone(self.pumpkin)

        self.obsFig = self.gw.getCanvas().create_image(self.cloned_obj.x, self.cloned_obj.y, image=self.cloned_obj.get_obstacle())
        self.pumpFig = self.gw.getCanvas().create_image(self.pump_obj.x, self.pump_obj.y, image=self.pump_obj.get_obstacle())
        self.clonned_ghost = self.facObj.clone(self.ghost)
        self.ghostFig = self.gw.getCanvas().create_image(self.clonned_ghost.x, self.clonned_ghost.y, image=self.clonned_ghost.get_obstacle())

    def ObsMotion(self):
        #Decrement x to make obstacles move
        self.clonned_ghost.x -= 5
        self.pump_obj.x -= 5
        self.gw.getCanvas().coords(self.ghostFig,self.clonned_ghost.x, self.clonned_ghost.y)
        self.gw.getCanvas().coords(self.obsFig,self.clonned_ghost.x, self.cloned_obj.y)
        self.gw.getCanvas().coords(self.pumpFig,self.pump_obj.x,self.pump_obj.y)
        
        # When obstacles go out of frame, bring them back in frame
        if self.clonned_ghost.x < -100 :
            self.score += 1
            self.gw.getCanvas().itemconfig(self.sWin, text=str(self.score))
            self.get_rand_obs()

        if self.gw.pause == False :
            self.gw.getWindow().after(20,self.ObsMotion)

    def DetectCollision(self):

        if (self.clonned_ghost.x < 150 and self.clonned_ghost.x + 100 >= 55) and ((self.gw.posY >= self.clonned_ghost.y - 10 and self.gw.posY < self.clonned_ghost.y + 10)  or (self.gw.posY >= self.cloned_obj.y - 100)):
            
            self.gw.pause = True
            self.ScoreBoard()
            self.EndGameScreen()
        
        if self.gw.pause == False :
            self.gw.getWindow().after(20,self.DetectCollision)

    def ScoreBoard(self):
        self.bestScore = 0

        if os.path.isfile("data.dat"):
            scoreFile = open('data.dat')
            self.bestScore = int(scoreFile.read())
            scoreFile.close()
        else:
            scoreFile = open('data.dat', 'w')
            scoreFile.write(str(self.bestScore))
            scoreFile.close()

        if self.score > self.bestScore:
            self.bestScore = self.score 
            scoreFile = open('data.dat', 'w')
            scoreFile.write(str(self.bestScore))
            scoreFile.close()
			
    def EndGameScreen(self):
        #self.endRectangle = self.gw.getCanvas().create_rectangle(0, 0, 550, 700, fill='#4EC0CA')
        self.endScore = self.gw.getCanvas().create_text(15, 200, text="Your score: " + str(self.score), font='Impact 50', fill='#FFFF00', anchor=W)
        self.endBest = self.gw.getCanvas().create_text(15, 280, text="Best score: " + str(self.bestScore), font='Impact 50', fill='#FFFF00', anchor=W)


    def RestartGame(self):

        self.gw.posY = 200
        self.clonned_ghost.x = 550
        self.score = 0
        self.gw.getCanvas().itemconfig(self.sWin, text=str(self.score))
        self.gw.pause = False
        self.gw.getCanvas().delete(self.endScore)
        #self.gw.getCanvas().delete(self.endRectangle)
        self.gw.getCanvas().delete(self.endBest)
        self.gw.getCanvas().delete(self.ghostFig)
        self.gw.getCanvas().delete(self.obsFig)

        self.gw.run()

    
