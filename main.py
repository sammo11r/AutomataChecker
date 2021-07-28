# AutomataChecker
# Author: Sam Nijsten
# Date: 28/07/2021

# Import the necessary libraries
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
import exrex

from DFA import checkDFA, validDFA
from print import printDFA

# Define variables for the set of states, set of final states, and the set of transitions
Q, F, D = [], [], []

# Main class, runs the applet
class main:
	def __init__(self, master):
		self.master = master
		master.title("AutomataChecker")

		master.rowconfigure([0, 1, 2, 3], minsize = 20)

		# Define the inputs to be tested
		test = Entry(master)
		test.grid(row = 0)

		# Check the DFA
		check = Button(master, text = 'Check DFA', command = lambda: checkdfa())
		check.grid(row = 1)

		# Print the DFA
		prnt = Button(master, text = 'Print DFA', command = lambda: printdfa(D, Q, F))
		prnt.grid(row = 2)

		# Reset
		reset = Button(master, text = 'Reset', command = lambda: reset())
		reset.grid(row = 3)

		# Define canvas 
		self.canvas = Canvas(master, width = 550, height = 650, bg = 'beige')
		self.canvas.grid(row = 4, sticky = "w", padx = 5, pady = 5)

		# Bind input
		self.canvas.bind('<Shift-1>', self.define_final)
		self.canvas.bind('<Button-1>', self.select_state)
		self.canvas.bind('<Button-3>', self.define_state)

		# Check the drawn DFA
		def checkdfa():
			check = validDFA(D)
			if not check[0]:
				showinfo("Your DFA is not valid", "State " + check[1] + 
					" seems to have multiple transitions on input " + check[2])
				return 0

			dfa = (D, Q[0][0], F)

			#Combine the input words into an array
			W = []
			words = test.get().split(",")

			# Check for regular expression
			if len(words) > 1:
				for w in words:
					# Remove spaces
					c = w.replace(" ", "")
					W.append(c)
			else:
				W = []
				for i in range(0, 2000):
					word = exrex.getone(words[0])
					if not word in W:
						W.append(word)
				print(W)

			# Check the validity of the DFA and produce a pop-up
			if checkDFA(dfa, W):
				result = "Your DFA is correct!"
			else:
				result = "Your DFA is incorrect..."

			showinfo("result", str(result))

		# Print the DFA as a 5-tuple
		def printdfa(D, Q, F):
			result = printDFA(D, Q, F)
			showinfo("The following has been copied to your clipboard", result)

		def reset():
			# Clear the canvas and reset the values
			self.canvas.delete("all")
			test.delete(0, 'end')
			del Q[:]
			del F[:]
			del D[:]

	def define_state(self, event):
		# Set the drawing parameters
		x, y, r = event.x, event.y, 20
		color = 'white'

		# Set the name of the state
		l = len(Q)
		name = "q" + str(l)

		# Denote the initial state with an incoming arrow
		if l == 0:
			self.canvas.create_line(x - 50, y, x - r, y, smooth = 'true', arrow = LAST)

		#Draw state
		self.canvas.create_oval(x - r, y - r, x + r, y + r, outline = 'black',
			fill = color, tags = (name))
		self.canvas.create_text(x, y, text = name, tag = name)

		#Add the state to the set of states Q
		Q.append((name, x, y))

	def define_final(self, event):
		#Get the closest element to the mouse click
		state = self.canvas.find_closest(event.x, event.y)

		#Get and transform the tag
		tag = self.canvas.itemcget(state, "tags").split(' ', 1)[0]

		#Denote the final state with a double circle
		for q in Q:
			if q[0] == tag:
				x, y, r = q[1], q[2], 18

		self.canvas.create_oval(x - r, y - r, x + r, y + r, outline = 'black',
			fill = 'white', tags = 'final')
		self.canvas.create_text(x, y, text = tag)

		#Add final state to the set of final states F
		F.append(tag)

	def select_state(self, event):
        #Get the closest elements to the mouse click
		states = self.canvas.find_overlapping(event.x - 5, event.y - 5,
			event.x + 5, event.y + 5)

		for state in states:
			# Get and transform the tag
			tag = self.canvas.itemcget(state, "tags").split(' ', 1)[0]

			if tag != 'current':
				break

		#Save the tag of the origin of the future transition
		global origin
		origin = tag

		#Save the x and y of the origin of the future transition
		for q in Q:
			if q[0] == tag:
				global sourcex, sourcey
				sourcex, sourcey = q[1], q[2]

		#Set the left button to choose the destination of the transition
		self.canvas.bind('<Button-1>', self.define_transition)

	def define_transition(self, event):
        # Get the closest elements to the mouse click
		states = self.canvas.find_overlapping(event.x - 5, event.y - 5,
			event.x + 5, event.y + 5)

		for state in states:
			# Get and transform the tag
			tag = self.canvas.itemcget(state, "tags").split(' ', 1)[0]

			if tag != 'current':
				break

		# Set the x and y values of the endpoints of the transition
		for q in Q:
			if q[0] == tag:
				endx, endy = q[1], q[2]

		def popup(self):
			self.w = popupWindow(self.master)
			self.master.wait_window(self.w.top)

		def entryValue(self):
			return self.w.value

		popup(self)

		try:
			inpt = entryValue(self)
		except AttributeError: 	
			# Check for pre-mature closure of entry window
			self.canvas.bind('<Button-1>', self.select_state)
			return

		# Define the transition tuple
		transition = (origin, tag, inpt, len(D))
		space = 0

		# Check if the transition already exists
		for d in D:
			if d[0] == origin and d[1] == tag and d[2] == inpt:
				self.canvas.bind('<Button-1>', self.select_state)
				return
			elif d[0] == origin and d[1] == tag:
				space += 1

		label = (' ' * space * 4) + inpt

		# Add the transition to the set of transitions
		D.append(transition)

		if tag == origin:
			self.canvas.create_line(sourcex, sourcey - 20, sourcex - 20, sourcey - 70, 
				sourcex - 50, sourcey - 30, sourcex - 13, sourcey - 13, smooth = 'true',
				arrow = LAST)
			self.canvas.create_text(sourcex - 45, sourcey - 45, text = label)
		else:
			#Define variables for the curvature of the line
			mid_x = (endx - sourcex) / 2
			mid_y = (endy - sourcey) / 2

			# Define an offset and middle point
			offsetx = -mid_x / 2
			offsety = -mid_y / 2

			prime_x = sourcex + mid_x + offsety
			prime_y = sourcey + mid_y + offsetx

			xO, xE = 1, -1

			if (sourcex > endx):
				xO, xE = -1, 1

			#Draw the transition
			self.canvas.create_line(sourcex + (20 * xO), sourcey, 
				prime_x, prime_y, endx + (20 * xE), endy, 
				smooth = 'true', arrow = LAST, tag = (len(D)))
			self.canvas.create_text(prime_x, prime_y, text = label)

		# Give back control
		self.canvas.bind('<Button-1>', self.select_state)

# Define the pop-up window for the input value
class popupWindow(object):

    def __init__(self, master):

        top = self.top = Toplevel(master)

        # Set the position of the popup window
        top_x = root.winfo_rootx()
        top_y = root.winfo_rooty()
        top.geometry(f'+{top_x}+{top_y}')

        # Add the input elements to the popup
        self.label = Label(top, text = "Specify Input")
        self.label.pack()
        self.entry = Entry(top)
        self.entry.pack()
        self.button = Button(top, text='Submit', command = self.cleanup)
        self.button.pack()

    def cleanup(self):
    	# Delete popup
        self.value = self.entry.get()
        self.top.destroy()

root = Tk()
root.resizable(False, False)
AutomataChecker = main(root)
root.mainloop()