from tkinter import *

class Animation(object):
	# Override these methods when creating your own animation
	def mousePressed(self, event): pass
	def keyPressed(self, event): pass
	def timerFired(self): pass
	def init(self): pass
	
	def redrawAll(self): pass
	
	# Call app.run(width,height) to get your app started
	def run(self, width=1300, height=900):
		# create the root and the canvas
		root = Tk()
		
		self.width = width
		self.height = height
		self.canvas = Canvas(root, width=width, height=height)
		self.canvas.pack()

		# set up events
		def redrawAllWrapper():
			self.canvas.delete(ALL)
			self.redrawAll()
			self.canvas.update()

		def mousePressedWrapper(event):
			self.mousePressed(event)
			redrawAllWrapper()

		def keyPressedWrapper(event):
			self.keyPressed(event)
			redrawAllWrapper()

		root.bind("<Button-1>", mousePressedWrapper)
		root.bind("<Key>", keyPressedWrapper)

		# set up timerFired events
		self.timerFiredDelay = 250 # milliseconds
		def timerFiredWrapper():
			self.timerFired()
			redrawAllWrapper()
			# pause, then call timerFired again
			self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
			
		# init and get timerFired running
		self.init()
		timerFiredWrapper()
		# and launch the app
		root.mainloop()
		print("Bye")
