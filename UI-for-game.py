from Animation import Animation
import random
from PIL import Image, ImageTk

class Layout(Animation):

	def init(self):
		self.table = UI.loadTable()
		self.background = UI.loadTBackGround()
		self.lights = UI.loadLights()
		self.greenLight = self.lights[0]
		self.yelllowLight = self.lights[1]
		self.redLight = self.lights[2]
		self.faces = UI.loadFaces()
		self.Comp1Face = [self.faces[0],self.faces[1]]
		self.Comp2Face = [self.faces[2],self.faces[3]]
		self.Comp3Face = [self.faces[4],self.faces[5]]
		self.trophy = UI.loadTrophy()
		self.UNO = "UNO!!"
		self.oops = "OOPS!"
		self.bubble = UI.loadBubble()
		self.button = UI.loadButton()


	def mousePressed(self,event):
		pass

	def keyPressed(self,event):
		pass

	def redrawAll(self):
		
		for back in self.background:
			self.canvas.create_image(650,450,image=back)

		for table in self.table:
			self.canvas.create_image(650,450,image=table)

		for light in self.lights:
			self.canvas.create_image(175,150,image=light)

		for faces in self.faces:
			self.canvas.create_image(100,450,image=faces)

		
		self.canvas.create_image(800,700,image=self.button[0])
		self.canvas.create_text(797,670, text = "SAY", font="Times 22 italic bold",fill="white")		
		self.canvas.create_text(800,700, text = "IT!", font="Times 22 italic bold",fill="white")
			

	def timerFired(self):
		pass

class UI(object):
	
	def __init__(self):
		pass

	def loadTBackGround():
		filename = "UI-IMAGES/sky.png"
		original = Image.open(filename)
		resized = original.resize((1300,900), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(resized)
		return [image]

	def loadTrophy():
		filename = "UI-IMAGES/trophy.png"
		original = Image.open(filename)
		resized = original.resize((250,150), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(resized)

		return [image]

	def loadTable():

		filename = "UI-IMAGES/newertable.png"
		original = Image.open(filename)
		resized = original.resize((650,350), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(resized)
		return [image]

	def loadLights():
		images = []
		name = ["green","yellow","red"]
		for color in name:
			filename = "UI-IMAGES/%slight.png" % color
			original = Image.open(filename)
			resized = original.resize((200,125), Image.ANTIALIAS)
			image = ImageTk.PhotoImage(resized)
			images.append(image)
		return images

	def loadFaces():
		images = [ ]
		i=1
		for num in range(6):
			filename = "UI-IMAGES/face%d.png" % i
			original = Image.open(filename)
			resized = original.resize((200,125), Image.ANTIALIAS)
			image = ImageTk.PhotoImage(resized)
			images.append(image)
			i+=1
		return images

	def legalExists(top,deck):
		for card in deck:
			if UNOCards.isLegal(card,top):
				return True
		return False

	def loadNum():
		images = [ ]
		i=2
		for num in range(3):
			filename = "UI-IMAGES/%d.png" % i
			original = Image.open(filename)
			resized = original.resize((550,350), Image.ANTIALIAS)
			image = ImageTk.PhotoImage(resized)
			images.append(image)
			i+=1
		return images

	def loadBubble():
		filename = "UI-IMAGES/realbubble.png"
		original = Image.open(filename)
		resized = original.resize((170,150), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(resized)
		return [image]
	
	def loadButton():
		filename = "UI-IMAGES/button.png"
		original = Image.open(filename)
		resized = original.resize((170,150), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(resized)
		return [image]







game=Layout()
game.run(1300,900)