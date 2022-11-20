from tkinter import *
import random
import os


class GameWindow(Frame):
    __instance = None

    @staticmethod
    def getInstance():
        if GameWindow.__instance == None:
            GameWindow()
        return GameWindow.__instance

    def __init__(self,master) -> None:
        super().__init__(master)
        if GameWindow.__instance != None:
            raise Exception("This class is a Singleton")
        else:
            GameWindow.__instance = self
       

        self.pack()
        self.w = Canvas(self, width = 550, height = 700, background = "#4EC0CA")  
        self.w.pack()
        its = self.witch()
        self.w.create_image(10,10, image=its,anchor=NW)
        self.mainloop()

    def witch(self):
        witchImg = PhotoImage(file="flyingwitch.gif")
        return witchImg


if __name__ == '__main__':
        root = Tk()
        root.title("Witchy Witch")
        root.geometry('550x700')
        gw = GameWindow(root)

        
    
  
 
    