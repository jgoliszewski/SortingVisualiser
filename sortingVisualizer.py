from tkinter import *
from tkinter import ttk
import random
from sortingAlgorithms import bubbleSort, bubbleSortPlus

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.maxsize(900,600)
root.config(bg='#b3b3b3')


#variables
algorithms = ['Bubble Sort','Bubble Sort Plus']
selected_alg = StringVar()
data = []
font = ('Arial',15)
bgColor = 'white'

#functions
def drawData(data, colorArray, finished=False):
	canvas.delete('all')
	canvas_height = 380
	canvas_width = 800
	x_width = (canvas_width) / (len(data) + 1)
	spacing = 5
	offset = x_width//2
	normalizedData = [i / max(data) for i in data]
	for i, height in enumerate(normalizedData):
		#top left
		x0 = i * x_width + offset + spacing
		y0 = canvas_height - height * 340
		#bottom right
		x1 = (i + 1) * x_width + offset
		y1 = canvas_height
 
		canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
		canvas.create_text(x0+x_width//3, y0, anchor=SW, text=str(data[i]))
	if finished:
		canvas.create_text(canvas_width//2, canvas_height//3, text='Finished!',font=('Arial',50))
	root.update_idletasks()

def Generate():
	global data
	minVal = int(minEntry.get())
	maxVal = int(maxEntry.get())
	size = int(sizeEntry.get())
	
	data = []
	for _ in range(size):
		data.append(random.randrange(minVal, maxVal + 1))
	
	drawData(data, ['red' for x in range(len(data))])

def startAlgorithm():
	global data
	if selected_alg.get() == "Bubble Sort":
		bubbleSort(data, drawData, speedScale.get())
	if selected_alg.get() == "Bubble Sort Plus":
		bubbleSortPlus(data, drawData, speedScale.get())

#frame loyout
UI_frame = Frame(root, width=800, height=200, bg='#a7a7a7')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=800, height=380, bg='#f2f2f2')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface
#Row[0]

algMenu = ttk.Combobox(UI_frame, 
	font = font,
	textvariable=selected_alg, 
	values=[alg for alg in algorithms])
algMenu.grid(row=0, columnspan=2, padx=5, pady=5)
algMenu.current(1)

speedScale = Scale(UI_frame,
				from_=0.1,
				to=2.0,
				length=150,
				digits=2, 
				resolution=0.1,
				orient=HORIZONTAL, 
				label='Select speed',
				font=font,
				relief='groove',
				bg=bgColor,
				highlightbackground='black')
speedScale.grid(row=0, column=2, padx=5, pady=5)


Button(UI_frame, 
	text="    Start    ", 
	font=font,
	justify='center',
	command=startAlgorithm, 
	bg='#00e30b',
	).grid(row=0, column=3, padx=5, pady=5)

#Row[1]

sizeEntry = Scale(UI_frame, 
	from_=5, 
	to=25, 
	orient=HORIZONTAL, 
	label='Data size', 
	font=font,
	bg=bgColor,
	highlightbackground='black')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, 
	from_=0, 
	to=10, 
	orient=HORIZONTAL, 
	label='Min Value',
	font=font,
	bg=bgColor,
	highlightbackground='black')
minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=E)

maxEntry = Scale(UI_frame, 
	from_=10, 
	to=100, 
	orient=HORIZONTAL, 
	label='Max Value',
	font=font,
	bg=bgColor,
	highlightbackground='black')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, 
	text="Generate", 
	command=Generate, 
	bg='#15b4ea', 
	font=font
	).grid(row=1, column=3, padx=5, pady=5)

root.mainloop()