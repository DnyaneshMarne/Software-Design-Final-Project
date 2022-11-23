from tkinter import *
import random
import os


class GameWindow:
    __instance = None
    @staticmethod
    def getInstance():
        if GameWindow.__instance == None:
            GameWindow()
        return GameWindow.__instance

    def __init__(self) -> None:
       
        if GameWindow.__instance != None:
            raise Exception("This class is a Singleton")
        else:
            GameWindow.__instance = self
            self.posY = 50
            self.posX = 50
            self.framerate = 20
            self.pause = False
            self.upcount = 0

            self._window=Tk()
            self._window.title("Witchy Witch")
            self._window.geometry('1000x800')
            self._window.resizable(width=False,height= False)
            self._canvas = Canvas(self._window, width = 1000, height = 800, background = "#4EC0CA")
            self._canvas.pack(expand= True)
            
            self.witchImg = PhotoImage(file="flyingwitch.gif")
            self._witch = self._canvas.create_image(self.posX,self.posY,image=self.witchImg)
            

    def witchDown(self):
        
        self.posY += 8
        if self.posY >= 800: 
            self.posY= 800
            self.pause = True
        self._canvas.coords(self._witch,self.posX, self.posY)    
        if self.pause == False :
            self._window.after(20,self.witchDown) 

    def witchUp(self,event = None):

        if self.pause == False: 
            self.posY-= 20
            if self.posY <= 0: self.posY = 0
            self._canvas.coords(self._witch,50, self.posY)  
            if self.upcount < 5:
                self.upcount += 1
                self._window.after(20,self.witchUp) 
               
            else: self.upcount = 0  


    def run(self):
        "Run application"
        self._window.after(20, self.witchDown)
        self._window.bind("<space>", self.witchUp)
        self._window.mainloop()


def main():
    "EntryPoint"
    gw = GameWindow()
    gw.run()

if __name__ == '__main__':
    main()

        
