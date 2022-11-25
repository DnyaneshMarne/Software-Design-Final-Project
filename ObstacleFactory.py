from tkinter import *
from PIL import Image
from abc import ABC,abstractmethod


class Obstacles(ABC) :

	def __init__(self):
		self.dir = "downsized_images/"
	
	@abstractmethod
	def get_obstacle(self,obs):
		pass


class Ghost(Obstacles):
	""" returns a ghost obstacle """
	def __init__(self):
		super().__init__()
		img = (Image.open("images/ghost.png"))
		resized_image= img.resize((150, 105), Image.LANCZOS)
		self.img = resized_image.save(self.dir + "downsize_ghost.png")

	def get_obstacle(self, obs):
		self.image = PhotoImage(file=self.dir + "downsize_ghost.png")
		return self.image

class Castle1(Obstacles):
	""" returns a castle1 obstacle """
	def __init__(self):
		super().__init__()
		img = (Image.open("images/castle1.png"))
		resized_image= img.resize((200, 405), Image.LANCZOS)
		self.im1 = resized_image.save(self.dir + "downsize_castle1.png")

	def get_obstacle(self, obs):
		self.image = PhotoImage(file=self.dir + "downsize_castle1.png")
		return self.image

class Castle2(Obstacles):
	""" returns a castle2 obstacle """
	def __init__(self):
		super().__init__()
		img = (Image.open("images/castle2.png"))
		resized_image= img.resize((200, 405), Image.LANCZOS)
		self.im1 = resized_image.save(self.dir + "downsize_castle2.png")

	def get_obstacle(self, obs):
		self.image = PhotoImage(file= self.dir + "downsize_castle2.png")
		return self.image

class Tree(Obstacles):
	""" returns a tree obstacle """
	def __init__(self):
		super().__init__()
		img = (Image.open("images/tree.png"))
		resized_image= img.resize((200, 405), Image.LANCZOS)
		self.im1 = resized_image.save(self.dir + "downsize_tree.png")

	def get_obstacle(self, obs):
		self.image = PhotoImage(file = self.dir + "downsize_tree.png")
		return self.image


class Factory():
	def __init__ (self):
		self.obstacles = {
		"Ghost": Ghost,
        "Castle1": Castle1,
        "Castle2": Castle2,
        "Tree": Tree,
	}

	def create(self,obstacle_name = "Ghost"):
		return self.obstacles[obstacle_name]()
