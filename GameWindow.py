from tkinter import *
from ObsDynamics import ObsDynamics
from PIL import Image

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
            self.posY = 200
            self.posX = 100
            self.framerate = 20
            self.pause = False 
            self.upcount = 0
            self._window=Tk()
            self._window.title("Witchy Witch")
            self._window.geometry('550x700')
            self._window.resizable(width=False,height= False)
            self._canvas = Canvas(self._window, width = 550, height = 700, background = "#10104E")
            img = (Image.open("Background.png"))
            resized_image= img.resize((550,600), Image.LANCZOS)
            self.im1 = resized_image.save("Background.png")
            self.background = PhotoImage(file="Background.png")
            self._backimage = self._canvas.create_image(0,0,anchor= NW, image=self.background)
            self._canvas.pack(expand= True)
            self.witchImg = PhotoImage(file="flyingwitch.png")
            self._witch = self._canvas.create_image(self.posX,self.posY,image=self.witchImg)
            self.Obstacles = ObsDynamics(self.getInstance())

    def witchDown(self):
        
        self.posY += 8
        if self.posY >= 700:   
            self.posY= 700
            self.pause = True
        self._canvas.coords(self._witch,self.posX, self.posY)    
        if self.pause == False :
            self._window.after(20,self.witchDown) 

    def witchUp(self,event = None):

        if self.pause == False: 
            self.posY-= 20
            if self.posY <= 0: self.posY = 0
            self._canvas.coords(self._witch, self.posX, self.posY)  
            if self.upcount < 5:
                self.upcount += 1
                self._window.after(20,self.witchUp) 
               
            else: self.upcount = 0  
        else: 
            self.Obstacles.RestartGame()

    def getCanvas(self):        
        return self._canvas
    def getWindow(self):
        return self._window

 
    def run(self):
        "Run application"

        self._window.after(20, self.witchDown)
        self._window.after(20,self.Obstacles.get_rand_obs)
        self._window.after(20,self.Obstacles.ObsMotion)
        self._window.after(20,self.Obstacles.DetectCollision)
        self._window.bind("<space>", self.witchUp)
        self._window.mainloop()




def main():

    "EntryPoint"
    gw = GameWindow.getInstance()
    gw.run()

if __name__ == '__main__':
    main()

        
