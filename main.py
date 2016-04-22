from Animation import Animation
from tkinter import *
import random 
import copy
from PIL import Image, ImageTk
import speech_recognition as sr

class UNOGame(Animation):
	
	def init(self):
		self.mode = "title"
		self.numOfPlayers = 2
		####################################
		# MAIN INIT
		####################################

		#general card stuff
		self.top=[ ]
		self.deck=UNODeck.deck
		self.drawdeck=[self.deck[0]]
		self.hand=UNOHand.hand
		self.hand=UNOHand.reGetHand(self.hand)
		self.top.append(self.deck.pop(-1))
		self.timerFiredDelay = 300
		self.startLength=7
		self.startLength1=7
		self.startLength2=7
		self.startLength3=7

		# UI IMAGES
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
		# number of computer players, changes to true based on how many Players selected
		

		"""BASED ON SELECTION, CHANGE LATER"""
		self.order=[ ]
		for num in range(self.numOfPlayers):
			num+=1
			self.order.append(num)
		self.turn=None
		print(self.order)
		# create a function that creates a list of number of players selected #2-4 plaYERS
		self.PlayerTurn=True
		self.Comp1Turn=False
		self.Comp2Turn=False
		self.Comp3Turn=False

		self.Comp1=True
		self.com1=CompHand1.comp1
		self.com1=CompHand1.reGetHand(self.com1)
		print(self.com1,"computers hand")

		self.Comp2=False
		if self.numOfPlayers > 2:
			self.Comp2 = True
		self.com2=CompHand2.comp2
		self.com3=CompHand2.reGetHand(self.com2)
		self.Comp3=False
		if self.numOfPlayers > 3:
			self.Comp3 = True
		self.com3=CompHand3.comp3
		self.com3=CompHand3.reGetHand(self.com3)

		self.PlayerUno = False
		self.DaveUNO = False
		self.RodgerUNO = False
		self.SallyUNO = False

		self.winner = None
		self.winnerFace = None
		self.trophy = UI.loadTrophy()
		self.UNO = "UNO!!"
		self.oops= "OOPS!"
		self.bubble = UI.loadBubble()
		self.UNOcount = 0
		self.button = UI.loadButton()

		#things for mistakes and deck
		self.going=None
		self.back=None
		self.drawn=None
		self.mistakeCount=0
		self.moveMade=None
		self.checking=False
		#this changes to True when the the top card holds these attributes and runs certain functions
		self.LegalExists=None
		self.wait=0
		self.GameOver=False
		self.Pause = False
		self.next=None
		self.test=None # card that you clicked and the card that you selected
		self.isReverse=False
		self.isSkip=False
		self.isDraw2=False
		self.isDraw4=False
		self.pickedUp=False
		self.mistakeCount=0
		self.cardImages = UNOCards.loadUnoCardImages()

		####################################
		# TitleScreen INIT
		####################################
		self.circles = [ ]
		self.timerFiredDelay = 70
		self.title = 0 
		self.titleImages = Dot.loadTitle()
		####################################
		# HELPScreen INIT
		####################################
		# same as Title Screen
		self.ovals = [ ]

		####################################
		# HELPScreen INIT
		####################################
		# same as title screen
		self.dots = [ ]
		self.numPics = Dot.loadNum()

	####################################
	# modeDispatcher
	####################################

	def mousePressed(self,event):
		if (self.mode=="title"): UNOGame.titlemousePressed(self,event)
		elif self.mode=="help": UNOGame.helpmousePressed(self,event)
		elif self.mode=="selection": UNOGame.selectionmousePressed(self,event)
		elif self.mode=="game": UNOGame.gamemousePressed(self,event)

	def keyPressed(self,event):
		if self.mode=="title": UNOGame.titlekeyPressed(self,event)
		elif self.mode=="help": UNOGame.helpkeyPressed(self,event)
		elif self.mode=="selection":
			if event.keysym=="2":
				self.numOfPlayers+=1

				print(self.numOfPlayers)
			elif event.keysym=="3":
				self.numOfPlayers+=2

			UNOGame.selectionkeyPressed(self,event)
		elif self.mode=="game": UNOGame.gamekeyPressed(self,event)

	def redrawAll(self):
		if self.mode=="title": UNOGame.titleredrawAll(self)
		elif self.mode=="help": UNOGame.helpredrawAll(self)
		elif self.mode=="selection": UNOGame.selectionredrawAll(self)
		elif self.mode=="game": UNOGame.gameredrawAll(self)

	def timerFired(self): 
		if self.mode=="title": UNOGame.titletimerFired(self)
		elif self.mode=="help": UNOGame.helptimerFired(self)
		elif self.mode=="selection": UNOGame.selectiontimerFired(self)
		elif self.mode=="game": UNOGame.gametimerFired(self)

	####################################
	# TITLE MODE
	####################################

	def titlemousePressed(self,event):
		pass

	def titlekeyPressed(self,event):
		if event.keysym=="space":
			self.mode = "help"
		

	def titleredrawAll(self):
		self.canvas.create_rectangle(0,0,1300,900,fill="black")
		for dot in self.circles:
			dot.draw(self.canvas)
		if self.title>30:
			self.canvas.create_image(250,250,image=self.titleImages[0])
		if self.title>40:
			self.canvas.create_image(1050,250,image=self.titleImages[1])
		if self.title>50:
			self.canvas.create_image(650,650,image=self.titleImages[2])
		if self.title>55:
			self.canvas.create_text(650,75,text="Press SPACE To Begin",fill="white",font="Times 28 italic")
			self.canvas.create_text(650,110,text="(Please wear headphones)",fill="white",font="Times 20 italic")
			self.canvas.create_text(150,750,text="Obed Appiah-Agyeman",fill="white",font="Times 20 italic")


	def titletimerFired(self):
		self.title+=1
		
		x = random.randint(550,750)
		r = random.randint(3,4)
		y = random.randint(1,900)
		self.circles.append(Dot(x,y,r))

		x = random.randint(550,750)
		r = random.randint(3,4)
		y = random.randint(1,900)
		self.circles.append(Dot(x,y,r))
		
		for dot in self.circles:
			dot.onTimerFired()
	
	####################################
	# HELP MODE
	####################################
	def helpmousePressed(self,event):
		pass

	def helpkeyPressed(self,event):
		if event.keysym=="space":
			self.mode = "selection"

	def helpredrawAll(self):
		self.canvas.create_rectangle(0,0,1300,900,fill="black")
		for dot in self.ovals:
			dot.draw(self.canvas)
		self.canvas.create_text(650,75,text="How To Play",fill="white",font="Times 28 italic underline")
		self.canvas.create_text(150,150,text="Objective:",fill="white",font="Times 20 italic underline")
		self.canvas.create_text(450,185,text="The goal of the game is to get rid of all your cards before anyone else",
		fill="white",font="Times 18 italic")
		self.canvas.create_text(435,250,text="Rules (Similar to Traditional UNO but several differences):",fill="white",font="Times 20 italic underline")
		self.canvas.create_text(535,285,text="- Match the top card with either a card of the same number or color",fill="white",font="Times 18 italic")
		self.canvas.create_text(500,320,text="- A Wild Card or A Wild Draw +4 can be placed on any card",fill="white",font="Times 18 italic")
		self.canvas.create_text(680,355,text="- If a Wild Card, is placed, you are allowed to place another Card as an example, (ONLY A WILD)",fill="white",font="Times 18 italic")
		self.canvas.create_text(730,390,text="- If you have no cards to play, you can click the deck to pick up or click 'SAY IT' and say 'PICK AND PLAY' ",fill="white",font="Times 18 italic")
		self.canvas.create_text(550,425,text="- If the card you picked up cannot be played, then your turn is forfeited",fill="white",font="Times 18 italic")
		self.canvas.create_text(425,460,text="- The traffic lights indicated whose turn it is",fill="white",font="Times 18 italic")
		self.canvas.create_text(450,495,text="- GREEN LIGHT: Your Turn",fill="white",font="Times 18 italic")
		self.canvas.create_text(450,525,text="- RED LIGHT: Opponent's Turn",fill="white",font="Times 18 italic")
		self.canvas.create_text(470,555,text="- YELLOW LIGHT: Checking For Mistake",fill="white",font="Times 18 italic")
		self.canvas.create_text(600,590,text="- If you see a mistake by the opponent press the 'SAY IT' button to say 'MISTAKE!' ",fill="white",font="Times 18 italic")
		self.canvas.create_text(720,630,text="- When you are about to have one card left press the 'SAY IT' button to say 'UNO' after you place the card",fill="white",font="Times 18 italic")
		self.canvas.create_text(700,665,text="- If you dont say UNO you are succeptible to being caught by the computer and having to draw 2 cards",fill="white",font="Times 18 italic")
		self.canvas.create_text(700,665,text="- If you dont say UNO you are succeptible to being caught by the computer and having to draw 2 cards",fill="white",font="Times 18 italic")
		self.canvas.create_text(500,700,text="- NO STACKING CARDS, only one card can be placed per turn",fill="white",font="Times 18 italic")
		self.canvas.create_text(650,770,text="PRESS SPACE TO CONTINUE",fill="white",font="Times 28 italic")
		
				



	def helptimerFired(self):

		x = random.randint(1,1300)
		r = random.randint(3,4)
		y = random.randint(1,900)
		self.ovals.append(Dot(x,y,r))
		
		for dot in self.ovals:
			dot.onTimerFired()
	####################################
	# SELECTION MODE
	####################################
	def selectionmousePressed(self,event):
		pass

	def selectionkeyPressed(self,event):
		if event.keysym=="1":
			self.timerFiredDelay = 300
			self.mode="game"
			#change data.mode
		elif event.keysym=="2":
			self.numOfPlayers+= 1
			self.timerFiredDelay = 300
			self.order.append(3)
			self.Comp2 = True
			self.mode="game"
			#change data.mode
		elif event.keysym=="3":
			self.numOfPlayers+= 2
			self.timerFiredDelay = 300
			self.order.append(3)
			self.order.append(4)
			self.Comp2 = True
			self.Comp3 = True
			self.mode="game"
			#change data.mode

	def selectionredrawAll(self):
		self.canvas.create_rectangle(0,0,1300,900,fill="black")
		for dot in self.dots:
			dot.draw(self.canvas)
		self.canvas.create_text(650,75,text="Press the corresponding key for the number of opponents",fill="white",font="Times 32 italic underline")
		
		self.canvas.create_image(300,250,image=self.numPics[0])
		self.canvas.create_text(500,225,text="Play with just Dave!",fill="white",font="Times 18 italic ")
		self.canvas.create_image(600,500,image=self.numPics[1])
		self.canvas.create_text(775,375,text="Play with Dave and Rodger!",fill="white",font="Times 18 italic ")
		self.canvas.create_image(900,750,image=self.numPics[2])
		self.canvas.create_text(1050,600,text="Play with Dave, Rodger, and Sally!",fill="white",font="Times 18 italic ")


	def selectiontimerFired(self):

		x = random.randint(1,1300)
		r = random.randint(3,4)
		y = random.randint(1,900)
		self.dots.append(Dot(x,y,r))
		
		for dot in self.dots:
			dot.onTimerFired()

	####################################
	# GAME MODE
	####################################
	def gamemousePressed(self,event):

		print(event.x,event.y)
		if UI.buttonContains(event.x,event.y):
			self.Pause = True
			if self.Pause == True:
				s = Speech.speech()
				if s == None:

					self.Pause = False

				elif "uno" in s:

					self.PlayerUno = True
					self.Pause = False

				elif "pick" in s or "a" in s:
					self.drawn = UNOHand.pickUp()
					self.pickedUp = True
					self.moveMade = True
					self.Pause = False

				elif "k" in s and "a" in s:
					if self.Comp1Turn==True:
						CompHand1.draw2()
						self.Pause = False
					elif self.Comp2Turn==True:
						CompHand2.draw2()
						self.Pause = False
					elif self.Comp3Turn==True:
						CompHand3.draw2()
						self.Pause = False

		if self.PlayerTurn==True: 
			if self.checking==False:
				for card in self.drawdeck:#will be code for "Pick and play", fix so that there is some pass function
					

					if card.deckContains(event.x,event.y) and self.pickedUp==False:
						# self.moveMade=True, test for pick and play
						self.drawn = UNOHand.pickUp()
						self.pickedUp = True
						self.moveMade=True
						print("deck happened") 
						print(len(self.hand), "<for some reason its this")

								

				for card in self.hand:
										
					if  card.handContains(event.x,event.y):
						self.test = card
						self.mistakeCount=0		
						# or self.top[0].kind=="Wild Draw +4" or self.top[0].kind=="Wild Card":
						a=self.hand.index(card)
						print(card)
					
						self.going=self.hand.pop(a)
						print(self.going)
						self.back=self.top[0]
						UNOCards.changePos(self.going,self.back)
						self.top.append(self.going)#if the card is in the hand change its x and y back to the original
						self.moveMade=True	

	def gamekeyPressed(self,event):
		if event.keysym=="r" and self.GameOver==True:
			UNOGame.init(self)

	def gameredrawAll(self):

	

		for back in self.background:
			self.canvas.create_image(650,450,image=back)

		for table in self.table:
			self.canvas.create_image(650,450,image=table)
			
		for card in self.drawdeck:
			image = self.cardImages[UNOCards.getUnoCardImage(card.kind,card.color)]

			back = self.cardImages[-1]
			card.draw(self.canvas,image,back)

		for card in self.hand:
			image=self.cardImages[UNOCards.getUnoCardImage(card.kind,card.color)]
			card.Hdraw(self.canvas,image)

		for card in self.top:

			image=self.cardImages[UNOCards.getUnoCardImage(card.kind,card.color)]
			card.topDraw(self.canvas,image)
		# SAY IT BUTTON
		self.canvas.create_image(800,700,image=self.button[0])
		self.canvas.create_text(797,670, text = "SAY", font="Times 22 italic bold",fill="white")		
		self.canvas.create_text(800,700, text = "IT!", font="Times 22 italic bold",fill="white")

		if self.checking==True:
			light = self.yelllowLight
		elif self.PlayerTurn==True:
			light = self.greenLight
		else:
			light = self.redLight

		self.canvas.create_image(600,700,image=light)		

		if self.Comp1==True:
			face=self.Comp1Face[1]
			self.canvas.create_image(650,75,image=face)

			if self.checking==True:
				light = self.yelllowLight
			elif self.Comp1Turn==True:
				light = self.greenLight
			else:
				light = self.redLight

			for card in self.com1:
				image=self.cardImages[UNOCards.getUnoCardImage(card.kind,card.color)]
				back = self.cardImages[-1]
				card.comp1Draw(self.canvas,back)
			# light was 850
			self.canvas.create_image(450,50,image=light)


		if self.Comp2==True:
			face=self.Comp2Face[0]
			self.canvas.create_image(80,450,image=face)
			if self.checking==True:
				light = self.yelllowLight
			elif self.Comp2Turn==True:
				light = self.greenLight
			else:
				light = self.redLight

			for card in self.com2:
				image=self.cardImages[UNOCards.getUnoCardImage(card.kind,card.color)]# how the card underit looks
				back = self.cardImages[-1]
				card.comp2Draw(self.canvas,back)

			self.canvas.create_image(75,300,image=light)

		if self.Comp3==True:
			face = self.Comp3Face[0]
			self.canvas.create_image(1210,450,image=face)
			if self.checking==True:
				light = self.yelllowLight
			elif self.Comp3Turn==True:
				light = self.greenLight
			else:
				light = self.redLight

			for card in self.com3:
				image=self.cardImages[UNOCards.getUnoCardImage(card.kind,card.color)]
				back = self.cardImages[-1]
				card.comp3Draw(self.canvas,back)
			#light was 580
			self.canvas.create_image(1200,300,image=light)


		if self.DaveUNO == True and self.UNOcount<5:

			self.canvas.create_image(835,100,image=self.bubble[0])
			self.canvas.create_text(820,75, text = self.UNO, font="Times 20 italic bold")
			if self.UNOcount >5:
				self.DaveUNO= False

		elif self.RodgerUNO == True  and self.UNOcount<5:

			self.canvas.create_image(80,650,image=self.bubble[0])
			self.canvas.create_text(65,630, text = self.UNO, font="Times 20 italic bold")
			if self.UNOcount >5:
				self.RodgerUNO= False

		elif self.SallyUNO == True  and self.UNOcount<5:
			
			self.canvas.create_image(1210,650,image=self.bubble[0])
			self.canvas.create_text(1195,630, text = self.UNO, font="Times 20 italic bold")

			if self.UNOcount >5:
				self.SallyUNO= False
		


		if self.GameOver:

			self.canvas.create_rectangle(350,250,950,650,fill="DeepSkyBlue2")
			self.canvas.create_text(525,350, text=self.winner,font="Times 34 italic")#replace with self.winner
			self.canvas.create_text(750,350, text="WINS!!!!!!!!!!!",font="Times 34 italic")
			self.canvas.create_image(550,450,image=self.winnerFace)#replace with self.winnerFace
			self.canvas.create_image(750,450,image=self.trophy[0])
			self.canvas.create_text(650,575, text = "Press R To Play Again!", font="Times 34 italic")

	def gametimerFired(self):

		if len(self.com1) == 1:
			self.DaveUNO = True
			self.UNOcount +=1

		elif len(self.com2) == 1:
			self.RodgerUNO = True
			self.UNOcount +=1

		elif len(self.com3) == 1:
			self.SallyUNO = True
			self.UNOcount +=1
			

		elif len(self.hand) == 1 :
			self.UNOcount=0
			self.UNOcount+=1
			if self.UNOcount>6:
				if self.PlayerUno==False:
					UNOHand.draw2()
					self.UNOcount=0
				else:
					self.UNOcount=0
					

		if len(self.hand)==0:
			self.winner = "YOU"
			self.GameOver = True

		elif len(self.com1) == 0:
			self.winnerFace = self.Comp1Face[0]
			self.winner = "Dave"
			self.GameOver = True
		elif len(self.com2) == 0:
			self.winnerFace = self.Comp2Face[0]
			self.winner = "Rodger"
			self.GameOver = True
		elif len(self.com3) == 0:
			self.winnerFace = self.Comp3Face[0]
			self.winner = "Sally"
			self.GameOver = True

		if not self.GameOver and not self.Pause:
		
			if self.next==True:

				if UNOCards.checkSkip(self.top)==True:
					self.order=UNOCards.skip(self.order)
					self.next=False

				elif UNOCards.checkReverse(self.top)==True:
					self.order=UNOCards.reverse(self.order)
					self.next=False

				else:
					self.order=UNOCards.changeOrder(self.order)
					self.next=False

			if self.order[0]==1:
				self.wait = 0
				self.PlayerTurn=True
				self.Comp1Turn=False
				self.Comp2Turn=False
				self.Comp3Turn=False

			elif self.order[0]==2:
				self.wait += 1
				self.PlayerTurn=False
				self.Comp1Turn=True
				self.Comp2Turn=False
				self.Comp3Turn=False

			elif self.order[0]==3:
				self.wait += 1
				self.PlayerTurn=False
				self.Comp1Turn=False
				self.Comp2Turn=True
				self.Comp3Turn=False

			elif self.order[0]==4:
				self.wait += 1
				self.PlayerTurn=False
				self.Comp1Turn=False
				self.Comp2Turn=False
				self.Comp3Turn=True	

			print(self.order[0])
			print("PlayersTurn:",self.PlayerTurn)
			print("Computers Turn:",self.Comp1Turn)
			print("Next:",self.next)
			print("Draw:",self.isDraw2)
			print("Draw:",self.isDraw4)
			print("MistakeCount:",self.mistakeCount)
			print(self.mistakeCount%20==0 and self.mistakeCount != 0)
			print("For some reason:",UNOCards.checkIsWild(self.top))
			print("check:",self.checking)
			print("wait:",self.wait)
			print("TopCard:",self.top)
			print("self:",self.test)

			

			if self.isDraw2==True:
				if self.PlayerTurn==True:

					UNOHand.draw2()
					self.isDraw2=False

				elif self.Comp1Turn==True:
					CompHand1.draw2()
					face=self.Comp1Face[1]
					self.isDraw2=False

				elif self.Comp2Turn==True:
					CompHand2.draw2()
					self.isDraw2=False

				elif self.Comp3Turn==True:
					CompHand3.draw2()
					self.isDraw2=False

			if self.isDraw4==True:

				if self.PlayerTurn==True:
					UNOHand.draw4()
					self.isDraw4=False

				elif self.Comp1Turn==True:
					CompHand1.draw4()
					face=self.Comp1Face[1]
					self.isDraw4=False

				elif self.Comp2Turn==True:
					CompHand2.draw4()
					self.isDraw4=False

				elif self.Comp3Turn==True:
					CompHand3.draw4()
					self.isDraw4=False

			if len(self.hand)>self.startLength or len(self.hand)<self.startLength:
				
				print("got redrawn")#print("got redrawn")
				self.startLength=len(self.hand)
				self.hand=UNOHand.reGetHand(self.hand)

			if len(self.com1)>self.startLength1 or len(self.com1)<self.startLength1:
				
				print("got redrawn")#print("got redrawn")
				self.startLength1=len(self.com1)
				self.com1=CompHand1.reGetHand(self.com1)
				if self.DaveUNO:
					self.UNOcount = 0
					
					self.DaveUNO = False 

			if len(self.com2)>self.startLength2 or len(self.com2)<self.startLength2:
				
				print("got redrawn")#print("got redrawn")
				self.startLength2=len(self.com2)
				self.com2=CompHand2.reGetHand(self.com2)
				if self.RodgerUNO:
					self.UNOcount = 0
					
					self.RodgerUNO = False

			if len(self.com3)>self.startLength3 or len(self.com3)<self.startLength3:
				
				print("got redrawn")#print("got redrawn")
				self.startLength3=len(self.com3)
				self.com3=CompHand3.reGetHand(self.com3)
				if self.SallyUNO:
					self.UNOcount = 0
				
					self.SallyUNO = False

	####################################
	# COMPUTER AI
	####################################
			if self.Comp1Turn==True and self.checking==False:
				
				if self.wait % 5==0 and self.wait !=0:
					self.LegalExists = CompHand1.legalExists(self.top,self.com1)

					if self.LegalExists == True:
						print(CompHand1.Comp1Move(self.com1,self.top))
						self.test = CompHand1.Comp1Move(self.com1,self.top)
						print(self.top)
						print(self.com1)
						self.mistakeCount=0
						if self.test==None:
							a= 0
						else:
							a = self.com1.index(self.test)

						self.going = self.com1.pop(a)
						print(self.going)
						self.back=self.top[0]
						UNOCards.changePos(self.going,self.back)
						self.top.append(self.going)#if the card is in the hand change its x and y back to the original
						self.moveMade=True
						self.wait = 0

					elif not self.LegalExists:
						if self.pickedUp == False:
							self.drawn = CompHand1.pickUp()
							self.pickedUp = True
							self.moveMade = True
							self.wait = 0

			elif self.Comp2Turn==True and self.checking==False:
				
				if self.wait % 5==0 and self.wait !=0:

					self.LegalExists = CompHand2.legalExists(self.top,self.com2)

					if self.LegalExists == True:
						print(CompHand1.Comp1Move(self.com1,self.top))
						self.test = CompHand2.Comp2Move(self.com2,self.top)
						print(self.top)
						print(self.com2)
						self.mistakeCount=0
						a = self.com2.index(self.test)
						self.going = self.com2.pop(a)
						print(self.going)
						self.back=self.top[0]
						UNOCards.changeYPos(self.going,self.back)
						self.top.append(self.going)#if the card is in the hand change its x and y back to the original
						self.moveMade=True
						self.wait = 0

					elif not self.LegalExists:
						if self.pickedUp == False:
							self.drawn = CompHand2.pickUp()
							self.pickedUp = True
							self.moveMade = True
							self.wait = 0

			elif self.Comp3Turn==True and self.checking==False:
				
				if self.wait % 5==0 and self.wait !=0:

					self.LegalExists = CompHand3.legalExists(self.top,self.com3)

					if self.LegalExists == True:
						print(CompHand1.Comp1Move(self.com1,self.top))
						self.test = CompHand3.Comp3Move(self.com3,self.top)
						print(self.top)
						print(self.com3)
						self.mistakeCount=0
						a = self.com3.index(self.test)
						self.going = self.com3.pop(a)
						print(self.going)
						self.back=self.top[0]
						UNOCards.changeYPos(self.going,self.back)
						self.top.append(self.going)#if the card is in the hand change its x and y back to the original
						self.moveMade=True
						self.wait = 0

					elif not self.LegalExists:
						if self.pickedUp == False:
							self.drawn = CompHand3.pickUp()
							self.pickedUp = True
							self.moveMade = True
							self.wait = 0

	####################################
	# COMPUTER AI
	####################################

			if self.moveMade:
				self.mistakeCount+=1
				self.checking=True

				if self.PlayerTurn:

					if self.pickedUp: 

						if UNOCards.isLegal(self.drawn,self.top)==False:
							self.next=UNOCards.checkIsWild(self.top)
							self.checking=False
							self.moveMade=False
							self.pickedUp=False

						else:

							self.pickedUp=False
							self.checking=False
							self.moveMade=False

					if self.mistakeCount%8 == 0 and self.mistakeCount != 0:

						if UNOCards.isLegal(self.test,self.top)==False:
							print("mistake ran")
							# UNOCards.changePos(self.back,self.going)
							self.hand.append(self.going)
							print(self.hand)
							self.top.pop(1)
							# self.top.append(self.back) possible dead code
							self.moveMade=False
							self.checking=False

						if UNOCards.isLegal(self.test,self.top):
							back=self.top.pop(0)
							UNOCards.changeDeckPos(back)
							self.deck.append(back)
							self.next = UNOCards.checkIsWild(self.top)
							self.isDraw2 = UNOCards.checkDraw2(self.top)
							self.isDraw4 = UNOCards.checkDraw4(self.top)
							self.pickedUp=False
							self.moveMade=False
							self.checking=False
							print("For some reason:",UNOCards.checkIsWild(self.top))
							print("you this happened")

				elif self.Comp1Turn:

					if self.pickedUp: 

						if UNOCards.isLegal(self.drawn,self.top)==False:
							self.next=UNOCards.checkIsWild(self.top)
							self.checking=False
							self.pickedUp=False
							self.moveMade=False
							self.wait = 0

						else:

							self.pickedUp=False
							self.checking=False
							self.moveMade=False
							self.wait = 0
							



					if self.mistakeCount%8==0 and self.mistakeCount != 0:

						if UNOCards.isLegal(self.test,self.top)==False:
							print("mistake ran")
							# UNOCards.changePos(self.back,self.going)
							self.com1.append(self.going)
							print(self.com1)
							self.top.pop(1)
							# self.top.append(self.back) possibel dead code
							self.moveMade=False
							self.checking=False
							self.wait = 0


						elif UNOCards.isLegal(self.test,self.top):
							back=self.top.pop(0)
							UNOCards.changeDeckPos(back)
							self.deck.append(back)
							self.next = UNOCards.checkIsWild(self.top)
							self.isDraw2 = UNOCards.checkDraw2(self.top)
							self.isDraw4 = UNOCards.checkDraw4(self.top)
							self.pickedUp=False
							self.moveMade=False
							self.checking=False
							self.wait = 0
							print("you this happened")

				elif self.Comp2Turn:

					if self.pickedUp: 

						if UNOCards.isLegal(self.drawn,self.top)==False:
							self.next=UNOCards.checkIsWild(self.top)
							self.checking=False
							self.pickedUp=False
							self.moveMade=False
							self.wait = 0

						else:

							self.pickedUp=False
							self.checking=False
							self.moveMade=False
							self.wait = 0

					if self.mistakeCount%8==0 and self.mistakeCount != 0:

						if UNOCards.isLegal(self.test,self.top)==False:
							print("mistake ran")
							# UNOCards.changePos(self.back,self.going)
							self.com2.append(self.going)
							print(self.com2)
							self.top.pop(1)
							# self.top.append(self.back) possibel dead code
							self.moveMade=False
							self.checking=False
							self.wait = 0

						elif UNOCards.isLegal(self.test,self.top):
							back=self.top.pop(0)
							UNOCards.changeDeckPos(back)
							self.deck.append(back)
							self.next = UNOCards.checkIsWild(self.top)
							self.isDraw2 = UNOCards.checkDraw2(self.top)
							self.isDraw4 = UNOCards.checkDraw4(self.top)
							self.pickedUp=False
							self.moveMade=False
							self.checking=False
							self.wait = 0
							print("you this happened")

				elif self.Comp3Turn:

					if self.pickedUp: 

						if UNOCards.isLegal(self.drawn,self.top)==False:
							self.next=UNOCards.checkIsWild(self.top)
							self.checking=False
							self.pickedUp=False
							self.moveMade=False
							self.wait = 0

						else:

							self.pickedUp=False
							self.checking=False
							self.moveMade=False
							self.wait = 0
							
					if self.mistakeCount%8==0 and self.mistakeCount != 0:

						if UNOCards.isLegal(self.test,self.top)==False:
							print("mistake ran")
							# UNOCards.changePos(self.back,self.going)
							self.com3.append(self.going)
							print(self.com3)
							self.top.pop(1)
							# self.top.append(self.back) possibel dead code
							self.moveMade=False
							self.checking=False
							self.wait = 0

						elif UNOCards.isLegal(self.test,self.top):
							back=self.top.pop(0)
							UNOCards.changeDeckPos(back)
							self.deck.append(back)
							self.next = UNOCards.checkIsWild(self.top)
							self.isDraw2 = UNOCards.checkDraw2(self.top)
							self.isDraw4 = UNOCards.checkDraw4(self.top)
							self.pickedUp=False
							self.moveMade=False
							self.checking=False
							self.wait = 0
							print("you this happened")
####################################
# CLASSES AND UI
####################################

class UNOCards(object): #adapted from lecture notes
	names = ["0", "1", "2", "3", "4", "5", "6", "7",
				   "8", "9", "Skip", "Reverse", "Draw +2","Wild Draw +4","Wild Card"]
	colors= ["black","blue", "green", "red", "yellow"]
	BLUE=0
	RED=2
	GREEN=1
	YELLOW=3
	width=1300	
	height=900
	# cardImages = Animation.loadUnoCardImages()

	def __init__(self,x,y,kind,color="black"):
		self.x=x
		self.y=y
		self.wide=50
		self.length=75
		self.kind=kind
		self.color=color
		self.d=(((self.wide**2)+(self.length**2))**.05)

	def __repr__(self):
		return (" A %s %s" %
				(UNOCards.colors[self.color],
				 UNOCards.names[self.kind]))

	def getHashables(self):
		return (self.kind, self.color) # return a tuple of hashables

	def __hash__(self):
		return hash(self.getHashables())

	def __eq__(self, other):
		return (isinstance(other, UNOCards) and
				(self.kind == other.kind) and
				(self.color == other.color))

####################################
# UNO FUNCTIONS
####################################

	def skip(L): #figure out skipping and reversing with start index or
		order=copy.deepcopy(L)
		for times in range(2):
			back=order.pop(0)
			order.append(back)
		return order

	def reverse(L):
		order=copy.deepcopy(L)
		if len(order)==2:
			return UNOCards.changeOrder(order)
		else:
			order.reverse()
			return order

	
	def changeOrder(L):
		order=copy.deepcopy(L)
		back=order.pop(0)
		order.append(back)
		return order

	def checkIsWild(top):
		if top[0].kind==14:
			return False
		else:
			return True

	def checkSkip(top):
		if top[0].kind==10:
			return True
		else:
			return False

	def checkReverse(top):
		if top[0].kind==11:
			return True
		else:
			return False

	def checkDraw2(top):
		if top[0].kind==12:
			return True
		else:
			return False

	def checkDraw4(top):
		if top[0].kind==13:
			return True
		else:
			return False

	def isLegal(card,top):
		if card.kind==top[0].kind or card.color==top[0].color:
			return True
		elif card.kind==13 or card.kind==14:
			return True
		elif top[0].kind==13 or top[0].kind==14:
			return True
		else:
			return False

	def changePos(going,back):
		going.x = back.x

	def changeYPos(going,back):
		going.y = back.y

	def changeDeckPos(back): # double check
		back.x = 650	


	def deckContains(self, x, y):
	
		return (self.x-75<x<self.x-25 and self.y-25<y<self.y+75)

	# def Hdraw(self,canvas,image):
	# 	Hx=self.x
	# 	Hy=750
	# 	canvas.create_image(Hx+50,Hy+75,image=image)

	def handContains(self, x, y):
		return (self.x+25<=x<self.x+self.wide+25 and 750<=y<=750+self.length+25)

	def com1Contains(self,x,y):
		return (self.x+25<=x<self.x+self.wide+25 and 100<=y<=100+self.length+25)

####################################
# GETTING UNO CARDS
####################################

	@staticmethod
	def getDeck(shuffled=True):
		deck=[ ]
		for times in range(2):
			for number in range(1,len(UNOCards.names)-2):
				for color in range(1,5):
					deck.append(UNOCards(UNOCards.width//2,UNOCards.height//2,number,color))

		for special in range(4):
			deck.append(UNOCards(UNOCards.width//2,UNOCards.height//2,13,0))
			deck.append(UNOCards(UNOCards.width//2,UNOCards.height//2,14,0))

		for color in range(1,len(UNOCards.colors)):
			deck.append(UNOCards(UNOCards.width//2,UNOCards.height//2,0,color))

		if (shuffled):
			random.shuffle(deck)
		return deck

	
	def loadUnoCardImages():
		card1,card2=52,48
		cardImages= [ ]
		i=1
		color=["black","blue","green","red","yellow"]
		for card1 in range(card1):
			if card1%13==0 and card1!=0:
				i+=1
			names= (card1%13)
			filename = "uno-cards-gif/%s%d.gif" % (color[i],names)
			original= Image.open(filename)
			resized = original.resize((50,75),Image.ANTIALIAS)
			image=ImageTk.PhotoImage(resized)
			# print(filename)
			cardImages.append(image)

		i=0
		for times in range(2):
			if times % 2 ==1 and times != 0:
				i=1
			names=[13,14]
			filename = "uno-cards-gif/%s%d.gif" % (color[0],names[i])
			# print(filename)
			original = Image.open(filename)
			resized = original.resize((50,75),Image.ANTIALIAS)
			image = ImageTk.PhotoImage(resized)
			cardImages.append(image)
		lastcard = Image.open("uno-cards-gif/back.png")
		lastchange = lastcard.resize((70,95),Image.ANTIALIAS)
		back = ImageTk.PhotoImage(lastchange)
		cardImages.append(back)

		return cardImages

	def getUnoCardImage(kind,color):
		if kind == 13 and color == 0:
			return 53
		if kind == 14 and color == 0:
			return 52
		else:
			index = ((color-1)*13)+kind
			
			return index
		

####################################
# UNO CARD DRAWINGS
####################################

	def draw(self,canvas,image,back):

		x=self.x-100
		y=self.y-50

		canvas.create_image(x+50,y+75,image=image)
		canvas.create_image(x+50,y+75,image=back)
		
		

	def Hdraw(self,canvas,image):
		Hx=self.x
		# Hy=750
		Hy=self.y+300
		canvas.create_image(Hx+50,Hy+75,image=image)
		# canvas.create_rectangle(Hx,Hy,Hx+self.wide,Hy+self.length,fill=UNOCards.colors[self.color])
		# canvas.create_text(Hx+self.wide//2,Hy+self.length//2,text=UNOCards.names[self.kind],fill="grey36",font="Arial 12 bold")

	def topDraw(self,canvas,image):
		x=self.x
		y=self.y-50
		canvas.create_image(x+50,y+75,image=image)

	def comp1Draw(self,canvas,image):
		Hx=self.x
		# Hy=100
		Hy=self.y-350
		canvas.create_image(Hx+50,Hy+75,image=image)

	def comp2Draw(self,canvas,image):
		Hx=self.x-470
		# Hy=100
		Hy=self.y-90
		canvas.create_image(Hx+50,Hy+75,image=image)

	def comp3Draw(self,canvas,image):
		Hx = self.x + 370
		# Hy=100
		Hy = self.y - 90
		canvas.create_image(Hx+50,Hy+75,image=image)	
		
	def getHand(deck):
		main = deck
		hand = [ ]
		change = 100
		for number in range (7):			
			n=random.randint(0,len(main)-1)
			item=main.pop(n)
			item.x=change
			
			hand.append(item)
			change+=100
		return hand

	def getCompHand(deck):
		main = deck
		hand = [ ]
		change = 100
		for number in range (7):			
			n=random.randint(0,len(main)-1)
			item=main.pop(n)
			item.y=change
			
			hand.append(item)
			change+=100
		return hand


####################################
# UNO Decks
####################################

class UNODeck(UNOCards):	
	deck = UNOCards.getDeck()
	
		
####################################
# UNO Hands
####################################
class UNOHand(UNOCards):
	hand=UNOCards.getHand(UNODeck.deck)

	def __init__(self,x,y,kind,color="black"):
		super().init(x,y,kind,color="black")
		self.x=200
		

	def reGetHand(deck):
		hand=[ ]
		change=350
		

		for card in deck:
			card.x=change
			if len(deck)>18:
				change+=25
			else:
				change+=50
			
		return deck


	def draw2():		
		for amount in range(2):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			UNOHand.hand.append(item)
	def draw4():		
		for amount in range(4):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			UNOHand.hand.append(item)

	def pickUp():
		for amount in range(1):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			UNOHand.hand.append(item)
		return item

	""" 
	Once you get the computer working shorten the iterations of the change in x for the regetHands
	"""
class CompHand1(UNOCards):
	comp1=UNOCards.getHand(UNODeck.deck)

	def __init__(self,x,y,kind,color="black"):
		super().init(x,y,kind,color="black")
		
		

	def reGetHand(deck):
		hand=[ ]
		change=450
		for card in deck:
			card.x=change
			change+=35
		return deck

	def draw2():		
		for amount in range(2):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			CompHand1.comp1.append(item)

	def draw4():		
		for amount in range(4):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			CompHand1.comp1.append(item)

	def pickUp():
		for amount in range(1):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			CompHand1.comp1.append(item)
		return item

	def count():
		return len(CompHand1.comp1)

	def legalExists(top,deck):
		for card in deck:
			if UNOCards.isLegal(card,top):
				return True
		return False

	def Comp1Move(deck,top):
		chance = random.randint(0,99)
		if chance >= 20:
			for card in deck:
				if UNOCards.isLegal(card,top):
					return card
		elif chance < 20:
			n = random.randint(0,len(deck)-1)
			return deck[n]
			
class CompHand2(UNOCards):
	comp2=UNOCards.getCompHand(UNODeck.deck)

	def __init__(self,x,y,kind,color="black"):
		super().init(x,y,kind,color="black")
		

	def reGetHand(deck):
		hand=[ ]
		change=300
		for card in deck:
			card.y=change
			change+=50
		return deck


	def draw2():		
		for amount in range(2):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			CompHand2.comp2.append(item)

	def draw4():		
		for amount in range(4):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			CompHand2.comp2.append(item)

	def pickUp():
		for amount in range(1):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			CompHand2.comp2.append(item)
		return item

	def legalExists(top,deck):
		for card in deck:
			if UNOCards.isLegal(card,top):
				return True
		return False

	def Comp2Move(deck,top):
		chance = random.randint(0,99)
		if chance >= 10:
			for card in deck:
				if UNOCards.isLegal(card,top):
					return card
		elif chance < 10:
			n = random.randint(0,len(deck)-1)
			return deck[n]

class CompHand3(UNOCards):
	comp3=UNOCards.getCompHand(UNODeck.deck)

	def __init__(self,x,y,kind,color="black"):
		super().init(x,y,kind,color="black")
		
	def reGetHand(deck):
		hand=[ ]
		change=300
		for card in deck:
			card.y=change
			change+=50
		return deck


	def draw2():		
		for amount in range(2):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			CompHand3.comp3.append(item)

	def draw4():		
		for amount in range(4):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			CompHand3.comp3.append(item)


	def pickUp():
		for amount in range(1):
			n=random.randint(0,len(UNODeck.deck)-1)
			item=UNODeck.deck.pop(n)
			CompHand3.comp3.append(item)
		return item

	def legalExists(top,deck):
		for card in deck:
			if UNOCards.isLegal(card,top):
				return True
		return False

	def Comp3Move(deck,top):
		chance = random.randint(0,99)
		if chance >= 25:
			for card in deck:
				if UNOCards.isLegal(card,top):
					return card
		elif chance < 25:
			n = random.randint(0,len(deck)-1)
			return deck[n]

####################################
# UI STUFF
####################################


class UI(object):
	
	def __init__(self):
		pass

	def loadTBackGround():
		filename = "UI-IMAGES/sky.png"
		original = Image.open(filename)
		resized = original.resize((1300,900), Image.ANTIALIAS)
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

	def loadTrophy():
		filename = "UI-IMAGES/trophy.png"
		original = Image.open(filename)
		resized = original.resize((250,150), Image.ANTIALIAS)
		image = ImageTk.PhotoImage(resized)

		return [image]

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

	def buttonContains(x,y):
		return (750< x <850 and 650 < y < 750)

class Dot (object):
	
	def __init__(self,x,y,r):

		self.x = x
		self.y = y
		self.r = r

	def draw (self,canvas):
		(cx,cy,r) = (self.x,self.y,self.r)
		
		color = ["blue", "green2", "red", "yellow"]
		i = random.randint(0,3)
		canvas.create_oval(cx-r,cy-r,cx+r,cy+r,fill=color[i])

	def onTimerFired(self):
		if self.x>650:
			self.x+=20	
		elif self.x<650:
			self.x-=20

	def loadTitle():
		name = ["saywhat","say","UNO"]
		images = []
		for i in range (len(name)):
			filename = "UI-IMAGES/%s.png" % name[i]

			original = Image.open(filename)
			resized = original.resize((450,350), Image.ANTIALIAS)
			image = ImageTk.PhotoImage(resized)
			images.append(image)
		return images

	def loadNum():
 		images = [ ]
 		i=1
 		for num in range(3):
 			filename = "UI-IMAGES/%d.png" % i
 			original = Image.open(filename)
 			resized = original.resize((200,250), Image.ANTIALIAS)
 			image = ImageTk.PhotoImage(resized)
 			images.append(image)
 			i+=1
 		return images

class Speech(object):

	def speech():
		r = sr.Recognizer()
		r.energy_threshold = 200
		with sr.Microphone() as source:
			audio = r.listen(source)
		try:
			s = r.recognize_google(audio)
			word = s.lower()
			return word
		except sr.UnknownValueError:
			print("Could not understand")
			return None
game= UNOGame()
game.run(1300,900)




