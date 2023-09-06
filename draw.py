
from tkinter import Tk, Canvas, Frame, BOTH, NW
from PIL import Image, ImageTk
import random

class Example(Frame):

	penDown = False
	eraserDown = False
	oldX, oldY = None, None
	colors = ['yellow','yellow']
	penSize = 8

	def __init__(self):
		super().__init__()

		self.initUI()


	def initUI(self):

		self.master.title("High Tatras")
		self.pack(fill=BOTH, expand=1)

		self.img = Image.open("range_doppler.png")
		self.tatras = ImageTk.PhotoImage(self.img)

		self.canvas = Canvas(self, width=self.img.size[0]+20,
		   height=self.img.size[1]+20)
		self.canvas.create_image(10, 10, anchor=NW, image=self.tatras)
		self.canvas.pack(fill=BOTH, expand=1)
		self.create_widgets()
        
	def create_widgets(self):
		#self.master.title("Paint")
		#self.pack(fill=BOTH, expand=1)
		#self.canvas = Canvas(self)        
		self.canvas.bind('<Motion>', self.draw) # draw on canvas
		self.canvas.bind('<ButtonPress-1>', self.penDown) # place the pen
		self.canvas.bind('<ButtonRelease-1>', self.penUp) # pick up the pen
		self.canvas.bind('<Double-Button-3>', self.clear) # clear canvas
		self.canvas.bind('<ButtonPress-3>', self.eraserDown) # place the eraser
		self.canvas.bind('<ButtonRelease-3>', self.eraserUp) # pick up the eraser
		self.canvas.bind('<MouseWheel>', self.changeSize) # change brush size'''
		#img = PhotoImage(file="range_doppler.png")      
		#self.canvas.create_image(20,20, anchor=NW, image=img)  
		#self.canvas.pack(fill=BOTH, expand=1)

		print("voila")

	def draw(self, event):
		#self.tatras = ImageTk.PhotoImage(self.img)      
		#self.canvas.create_image(20,20, image=self.tatras) 
		x, y = event.x, event.y
		#for some reason using self.penDown alone will always pass as true
		#during initial call, even though it's initialized as False
		if self.penDown == True:
			self.last = self.canvas.create_line(self.oldX, self.oldY, x, y, width=self.penSize,fill=random.choice(self.colors),stipple="gray50")
		if self.eraserDown == True:
			items = self.canvas.find_overlapping(max(0, x-(self.penSize//2)), max(0, y-(self.penSize//2)), min(500,x+(self.penSize//2)), min(500,y+(self.penSize//2)))
			for x in items:
				self.canvas.delete(x)
		
		self.canvas.pack(fill=BOTH, expand=1)
		self.oldX = x
		self.oldY = y

	def penDown(self, event):
		self.penDown = True

	def penUp(self, event):
		self.penDown = False

	def clear(self, event):
		print("test")
		self.canvas.delete("all")

	def eraserDown(self, event):
		self.eraserDown = True

	def eraserUp(self, event):
		self.eraserDown = False

	def changeSize(self, event):
		num = event.delta // 120
		self.penSize += num
		if self.penSize > 10:
			self.penSize = 10
		if self.penSize < 1:
			self.penSize = 1       


def main():

	root = Tk()
	ex = Example()
	root.attributes('-alpha', 0.6)
	root.mainloop()


if __name__ == '__main__':
	main()
