from tkinter import *
from PIL import Image,ImageTk
import random
import os

FRAMERATE = 20
SCORE = -1

class Ghost:
	""" returns a ghost obstacle """

	def __init__(self):
		img = (Image.open("images/ghost.png"))
		resized_image= img.resize((150, 105), Image.Resampling.LANCZOS)
		im1 = resized_image.save("downsized_images/downsize_ghost.png")

	def get_obstacle(self, msg):
		self.image = PhotoImage(file="downsized_images/downsize_ghost.png")
		return self.image

class Castle1:
	""" returns a castle1 obstacle """

	def __init__(self):
		img = (Image.open("images/castle1.png"))
		resized_image= img.resize((150, 105), Image.Resampling.LANCZOS)
		im1 = resized_image.save("downsized_images/downsize_castle1.png")

	def get_obstacle(self, msg):
		self.image = PhotoImage(file="downsized_images/downsize_castle1.png")
		return self.image

class Castle2:
	""" returns a castle2 obstacle """

	def __init__(self):
		img = (Image.open("images/castle2.png"))
		resized_image= img.resize((150, 105), Image.Resampling.LANCZOS)
		im1 = resized_image.save("downsized_images/downsize_castle2.png")

	def get_obstacle(self, msg):
		self.image = PhotoImage(file="downsized_images/downsize_castle2.png")
		return self.image

class Tree:
	""" returns a tree obstacle """

	def __init__(self):
		img = (Image.open("images/tree.png"))
		resized_image= img.resize((150, 105), Image.Resampling.LANCZOS)
		im1 = resized_image.save("downsized_images/downsize_tree.png")

	def get_obstacle(self, msg):
		self.image = PhotoImage(file="downsized_images/downsize_tree.png")
		return self.image

def Factory(obstacle ="Ghost"):
	"""Factory Method"""
	obstacles = {
		"Ghost": Ghost,
        "Castle1": Castle1,
        "Castle2": Castle2,
        "Tree": Tree,
	}
	return obstacles[obstacle]()

g = Factory("Ghost")
c1 = Factory("Castle1")
c2 = Factory("Castle2")
t = Factory("Tree") 

obsDic = {}
obsDic['t'] = "Tree"
obsDic['c1'] = "Castle1"
obsDic['c2'] = "Castle2"

def center(toplevel):
	toplevel.update_idletasks()
	w = toplevel.winfo_screenwidth()
	h = toplevel.winfo_screenheight()
	size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
	x = w/2 - size[0]/2
	y = h/2 - size[1]/2 - 35
	toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
	
main = Tk()
main.resizable(width = False, height = False)
main.title("Flappy Bird")
main.geometry('550x700')

center(main)

BIRD_Y = 200
PIPE_X = 550
PIPE_HOLE = 0
OBS_POS = 0
NOW_PAUSE = False

BEST_SCORE = 0

if os.path.isfile("data.dat"):
	scoreFile = open('data.dat')
	BEST_SCORE = int(scoreFile.read())
	scoreFile.close()
else:
	scoreFile = open('data.dat', 'w')
	scoreFile.write(str(BEST_SCORE))
	scoreFile.close()

w = Canvas(main, width = 550, height = 700, background = "#4EC0CA", bd=0, highlightthickness=0)
w.pack()

birdImg = PhotoImage(file="images/bird.png")
bird = w.create_image(100, BIRD_Y, image=birdImg)

pipeDown = w.create_image(PIPE_X, PIPE_HOLE, image=g.get_obstacle("Ghost"))

res = key, val = random.choice(list(obsDic.items()))
if res[0] == 't':
	obsFig = w.create_image(PIPE_X, OBS_POS, image=t.get_obstacle("Tree"))
if res[0] == 'c1':
	obsFig = w.create_image(PIPE_X, OBS_POS, image=c1.get_obstacle("Castle1"))
else:
	obsFig = w.create_image(PIPE_X, OBS_POS, image=c2.get_obstacle("Castle2"))

up_count = 0
endRectangle = endBest = endScore = None

score_w = w.create_text(15, 45, text="0", font='Impact 60', fill='#ffffff', anchor=W)

def generatePipeHole():
	global PIPE_HOLE
	global OBS_POS
	global SCORE
	global FRAMERATE
	SCORE += 1
	w.itemconfig(score_w, text=str(SCORE))
	PIPE_HOLE = random.randint(100, 300)
	OBS_POS = random.randint(600, 600)
	
	#print("Score: " + str(SCORE))

generatePipeHole()

def birdUp(event = None):
	global BIRD_Y
	global up_count
	global NOW_PAUSE
	
	if NOW_PAUSE == False: 
		BIRD_Y -= 20
		if BIRD_Y <= 0: BIRD_Y = 0
		w.coords(bird, 100, BIRD_Y)
		if up_count < 5:
			print(up_count)
			up_count += 1
			main.after(FRAMERATE, birdUp)
		else: up_count = 0
	else:
		restartGame()

def birdDown():
	global BIRD_Y
	global NOW_PAUSE

	BIRD_Y += 8
	if BIRD_Y >= 700: BIRD_Y = 700
	w.coords(bird, 100, BIRD_Y)
	if NOW_PAUSE == False: main.after(FRAMERATE, birdDown)

def pipesMotion():
	global PIPE_X
	global PIPE_HOLE
	global NOW_PAUSE
	global OBS_POS
	global obsFig

	PIPE_X -= 5
	#w.coords(pipeUp, PIPE_X, 0, PIPE_X + 100, PIPE_HOLE)
	w.coords(pipeDown, PIPE_X, PIPE_HOLE)
	w.coords(obsFig, PIPE_X, OBS_POS)
	
	if PIPE_X < -100: 
		PIPE_X = 550
		res = key, val = random.choice(list(obsDic.items()))
		if res[0] == 't':
			obsFig = w.create_image(PIPE_X, OBS_POS, image=t.get_obstacle("Tree"))
		elif res[0] == 'c1':
			obsFig = w.create_image(PIPE_X, OBS_POS, image=c1.get_obstacle("Castle1"))
		elif res[0] == 'c2':
			obsFig = w.create_image(PIPE_X, OBS_POS, image=c2.get_obstacle("Castle2"))
		generatePipeHole()
	
	if NOW_PAUSE == False: main.after(FRAMERATE, pipesMotion)

def engGameScreen():
	global endRectangle
	global endScore
	global endBest
	endRectangle = w.create_rectangle(0, 0, 550, 700, fill='#4EC0CA')
	endScore = w.create_text(15, 200, text="Your score: " + str(SCORE), font='Impact 50', fill='#ffffff', anchor=W)
	endBest = w.create_text(15, 280, text="Best score: " + str(BEST_SCORE), font='Impact 50', fill='#ffffff', anchor=W)

def detectCollision():
	global NOW_PAUSE
	global BEST_SCORE

	print("Pipe: ", PIPE_X)
	print("Pipe hole:", PIPE_HOLE)
	print("Bird: ", BIRD_Y)

	if (PIPE_X < 150 and PIPE_X + 100 >= 55) and ((BIRD_Y >= PIPE_HOLE - 10 and BIRD_Y < PIPE_HOLE + 10) or (BIRD_Y >= OBS_POS)):
		#print("Collision")
		NOW_PAUSE = True
		if SCORE > BEST_SCORE:
			BEST_SCORE = SCORE
			scoreFile = open('data.dat', 'w')
			scoreFile.write(str(BEST_SCORE))
			scoreFile.close()
		#print("Pause")
		engGameScreen()
	if NOW_PAUSE == False: main.after(FRAMERATE, detectCollision)

def restartGame():
	global PIPE_X
	global BIRD_Y
	global SCORE
	global NOW_PAUSE
	global FRAMERATE

	BIRD_Y = 200
	PIPE_X = 550
	SCORE = -1
	FRAMERATE = 20
	NOW_PAUSE = False
	w.delete(endScore)
	w.delete(endRectangle)
	w.delete(endBest)
	generatePipeHole()
	main.after(FRAMERATE, birdDown)
	main.after(FRAMERATE, pipesMotion)
	main.after(FRAMERATE, detectCollision)
	
main.after(FRAMERATE, birdDown)
main.after(FRAMERATE, pipesMotion)
main.after(FRAMERATE, detectCollision)
main.bind("<space>", birdUp)
main.mainloop()