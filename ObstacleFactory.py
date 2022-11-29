from tkinter import *
from PIL import Image
from abc import ABC,abstractmethod
import copy
import random

class Obstacles(ABC) :

	def __init__(self,x=650,y=670,name = 'NotGhost'):
		self.dir = "downsized_images/"
		self.x = x
		self.y = y
		self.name = name
	
	@abstractmethod
	def get_obstacle(self):
		pass


class Ghost(Obstacles):
	""" returns a ghost obstacle """
	def __init__(self,x=650,y=670,name = 'Ghost'):
		super().__init__(x,y,name)
		img = (Image.open("images/ghost.png"))
		resized_image= img.resize((150, 105), Image.LANCZOS)
		self.img = resized_image.save(self.dir + "downsize_ghost.png")
		

	def get_obstacle(self):
		self.image = PhotoImage(file=self.dir + "downsize_ghost.png")
		return self.image

class Castle1(Obstacles):
	""" returns a castle1 obstacle """
	def __init__(self,x=650,y=670,name = 'Castle1'):
		super().__init__(x,y,name)
		img = (Image.open("images/castle1.png"))
		resized_image= img.resize((200, 405), Image.LANCZOS)
		self.im1 = resized_image.save(self.dir + "downsize_castle1.png")

	def get_obstacle(self):
		self.image = PhotoImage(file=self.dir + "downsize_castle1.png")
		return self.image

class Castle2(Obstacles):
	""" returns a castle2 obstacle """
	def __init__(self,x=650,y=670,name = 'Castle2'):
		super().__init__(x,y,name)
		img = (Image.open("images/castle2.png"))
		resized_image= img.resize((200, 405), Image.LANCZOS)
		self.im1 = resized_image.save(self.dir + "downsize_castle2.png")

	def get_obstacle(self):
		self.image = PhotoImage(file= self.dir + "downsize_castle2.png")
		return self.image

class Tree(Obstacles):
	""" returns a tree obstacle """
	def __init__(self,x=650,y=670,name = 'Tree'):
		super().__init__(x,y,name)
		img = (Image.open("images/tree.png"))
		resized_image= img.resize((200, 405), Image.LANCZOS)
		self.im1 = resized_image.save(self.dir + "downsize_tree.png")

	def get_obstacle(self):
		self.image = PhotoImage(file = self.dir + "downsize_tree.png")
		return self.image


class House(Obstacles):
	""" returns a tree obstacle """
	def __init__(self,x=650,y=670,name = 'House'):
		super().__init__(x,y,name)
		img = (Image.open("images/house.png"))
		resized_image= img.resize((200, 405), Image.LANCZOS)
		self.im1 = resized_image.save(self.dir + "downsize_house.png")

	def get_obstacle(self):
		self.image = PhotoImage(file = self.dir + "downsize_house.png")
		return self.image

class Pumpkin(Obstacles):
	""" returns a tree obstacle """
	def __init__(self,x=650,y=670,name = 'Pumpkin'):
		super().__init__(x,y,name)
		img = (Image.open("images/pumpkin.png"))
		resized_image= img.resize((100, 100), Image.LANCZOS)
		self.im1 = resized_image.save(self.dir + "downsize_pumpkin.png")
		

	def get_obstacle(self):
		self.image = PhotoImage(file = self.dir + "downsize_pumpkin.png")
		return self.image




class Factory():
	def __init__ (self):
		self.obstacles = {
		"Ghost": Ghost,
       		"Castle1": Castle1,
        	"Castle2": Castle2,
       		"Tree": Tree,
		"House" : House,
		"Pumpkin" : Pumpkin
	}

	def create(self,obstacle_name = "Ghost",x=0,y=0):
		return self.obstacles[obstacle_name](x,y)
	
	def clone(self,obj):
		newObj = copy.deepcopy(obj)
		if newObj.name == 'Ghost':
			newObj.y = random.randint(50, 330)
		return newObj
