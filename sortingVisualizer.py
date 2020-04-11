from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubbleSort, bubbleSortPlus
from quickSort import quickSort
from mergeSort import mergeSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from coktailSort import coktailSort
from bucketSort import bucketSort

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry('900x630')
root.maxsize(900,630)
root.config(bg='#b3b3b3')


#variables
selected_alg = StringVar()
ownData = IntVar()
randomData = IntVar()
stairsData = IntVar()
data = []
comp = 0

font = ('Arial',15)
green = '#00e30b'
orange = '#ffa500'

#functions
def drawData(data, colorArray, finished=False, pointer=-10, pivot=None, border=None, comprasions=0, maxValue=0):
	canvas.delete('all')
	canvas_height = 380
	canvas_width = 870
	x_width = (canvas_width) / (len(data) + 1)
	spacing = 5
	offset = x_width//2
	if maxValue == 0:
		normalizedData = [i / max(data) for i in data]
	else:
		normalizedData = [i / maxValue for i in data]

	for i, height in enumerate(normalizedData):
		#top left
		x0 = i * x_width + offset + spacing
		y0 = canvas_height - height * 320
		#bottom right
		x1 = (i + 1) * x_width + offset 
		y1 = canvas_height

		xp = pointer * x_width + offset + spacing
		canvas.create_text(xp+x_width/2-30, 
						26, 
						anchor=SW, 
						text='Pointer',
						font=font)
		canvas.create_rectangle(x0, y0, x1, y1, 
						fill=['#15b4ea' if i == pivot else colorArray[i]])
		if not stairsData.get():
			canvas.create_text(x0+x_width/2-10, 
						y0, 
						anchor=SW, 
						text=str(data[i]),
						font=font)
		if not finished:
			comprasionCanvas.delete('all')
			comprasionCanvas.create_text(
				50,
				34,
				font=('Arial',35),
				text=str(comprasions))
	if pivot != None and border != None:
		xp = pivot * x_width + offset + spacing
		xb = border * x_width + offset + spacing
		yp = canvas_height - normalizedData[pivot] * 320

		canvas.create_text(
			xp+x_width/2-25, 
			yp-30 if yp > 240 else yp + 30, 
			anchor=SW, 
			text='Pivot',
			font=font)
		canvas.create_text(
			xb+x_width/2-30, 
			43, 
			anchor=SW, 
			text='Border',
			font=font)

	if finished:
		canvas.create_text(canvas_width//2, 
						50, 
						text='Finished!',
						font=('Arial',50))

	root.update_idletasks()

def Generate():
	global data
	minVal = int(minEntry.get())
	maxVal = int(maxEntry.get())
	size = int(sizeEntry.get())
	data = []

	if ownData.get():
		try:
			data = [int(x) for x in dataOwn.get().split(', ')]
		except:
			try:
				data = [int(x) for x in dataOwn.get().split(' ')]
			except:
				try:
					data = [int(x) for x in dataOwn.get().split(',')]
				except:
					canvas.delete('all')
					canvas.create_text(380, 130, text='Wrong data!',font=('Arial',50))
	
	if randomData.get():
		for _ in range(size):
			data.append(random.randrange(minVal, maxVal + 1))

	if stairsData.get():	
		for i in range(size):
			data.append(i+1)
		random.shuffle(data)

	if data:
		drawData(data, ['red' for x in range(len(data))])
'''
def startAlgorithm(alg):
	print(alg)
	if alg == 'bubble':
		bubbleSort(data, drawData, speedScale.get(), [])

	elif alg == 'bubblePlus':
		bubbleSortPlus(data, drawData, speedScale.get(), [])
	elif alg == 'insertion':
		insertionSort(data, drawData, speedScale.get())
	elif alg == 'selection':
		selectionSort(data, drawData, speedScale.get(), [])
	elif alg == 'coktail':
		coktailSort(data, drawData, speedScale.get(), [])
	elif alg == 'merge':
		mergeSort(data, drawData, speedScale.get(), max(data), 0)
	elif alg == 'quick':
		quickSort(data, 0, len(data)-1, drawData, speedScale.get(), [], 0)
	elif alg == 'bucket':
		bucketSort(data, drawData, speedScale.get())
	drawData(data, [green for x in range(len(data))], finished=True)
'''
def bubble():
	global data
	global comp
	bubbleSort(data, drawData, speedScale.get(), [])
	drawData(data, [green for x in range(len(data))], finished=True)

def bubblePlus():
	global data
	global comp
	bubbleSortPlus(data, drawData, speedScale.get(), [])
	drawData(data, [green for x in range(len(data))], finished=True)

def insertion():
	global data
	global comp
	insertionSort(data, drawData, speedScale.get())
	drawData(data, [green for x in range(len(data))], finished=True)

def merge():
	global data
	global comp
	mergeSort(data, drawData, speedScale.get(), max(data), 0)
	drawData(data, [green for x in range(len(data))], finished=True)

def quick():
	global data
	global comp
	quickSort(data, 0, len(data)-1, drawData, speedScale.get(), [], 0)
	drawData(data, [green for x in range(len(data))], finished=True)

def selection():
	global data
	global comp
	selectionSort(data, drawData, speedScale.get(), [])
	drawData(data, [green for x in range(len(data))], finished=True)

def coktail():
	global data
	global comp
	coktailSort(data, drawData, speedScale.get(), [])
	drawData(data, [green for x in range(len(data))], finished=True)

def bucket():
	global data
	global comp
	bucketSort(data, drawData, speedScale.get())
	drawData(data, [green for x in range(len(data))], finished=True)

#frame loyout
UI_frame = Frame(
	root, 
	width=1000, 
	bg='#a7a7a7',
	borderwidth=5,
	relief=RIDGE)
UI_frame.grid(
	row=0, 
	column=0, 
	columnspan=2, 
	padx=10, 
	pady=2)

algorithms_frame = Frame(
	root, 
	bg='#a7a7a7',
	borderwidth=5,
	relief=RIDGE)
algorithms_frame.grid(
	row=1, 
	column=0, 
	columnspan=2, 
	padx=10, 
	pady=2, 
	sticky=W)

canvas = Canvas(
	root, 
	width=870, 
	height=380, 
	bg='#f2f2f2', 
	relief=RIDGE, 
	bd=3)
canvas.grid(
	row=2, 
	column=0, 
	columnspan=2, 
	padx=10, 
	pady=2, 
	sticky=N)

comprasionCanvas = Canvas(
	root, 
	width=100, 
	height=60, 
	bg='#f2f2f2', 
	relief=RIDGE, 
	bd=3)
comprasionCanvas.grid(
	row=1, 
	column=1, 
	padx=10, 
	pady=2, 
	sticky=E)

# scales
speedScale = Scale(
	UI_frame,
	from_=0,
	to=5,
	length=200,
	digits=2, 
	resolution=0.1,
	orient=HORIZONTAL, 
	label='Select Delay [s]',
	font=font,
	relief='groove',
	bg='white',
	highlightbackground='black')
speedScale.grid(
	row=0, 
	rowspan=2, 
	column=4, 
	columnspan=2, 
	padx=5, 
	pady=5, 
	sticky=N)

sizeEntry = Scale(
	UI_frame, 
	from_=5, 
	to=64, 
	orient=HORIZONTAL, 
	label='Data size', 
	font=font,
	bg='white',
	highlightbackground='black')
sizeEntry.grid(
	row=0, 
	rowspan=2, 
	column=1, 
	padx=5, 
	pady=5, 
	sticky=N)

minEntry = Scale(
	UI_frame, 
	from_=0, 
	to=10, 
	orient=HORIZONTAL, 
	label='Min Value',
	font=font,
	bg='white',
	highlightbackground='black')
minEntry.grid(
	row=0, 
	rowspan=2, 
	column=2, 
	padx=5, 
	pady=5, 
	sticky=N)

maxEntry = Scale(
	UI_frame, 
	from_=10, 
	to=100, 
	orient=HORIZONTAL, 
	label='Max Value',
	font=font,
	bg='white',
	highlightbackground='black')
maxEntry.grid(
	row=0, 
	rowspan=2, 
	column=3, 
	padx=5, 
	pady=5, 
	sticky=N)

# entry
dataOwn = Entry(
	UI_frame, 
	font=font, 
	width=30)
dataOwn.insert(END,'1, 2, 3 or 1,2,3 or 1 2 3 ')
dataOwn.grid(
	row=2, 
	columnspan=3,
	column=1, 
	padx=5, 
	pady=5)

# checkbuttons
checkDataOwn = Checkbutton(
	UI_frame, 
	bg='#a7a7a7',
	text='Your data', 
	font=font, 
	variable=ownData,
	relief=RIDGE,
	bd=3)
checkDataOwn.grid(
	row=2, 
	column=0, 
	padx=5, 
	pady=5, 
	sticky=W)

checkDataRandom = Checkbutton(
	UI_frame, 
	bg='#a7a7a7', 
	text='Random data', 
	font=font, 
	variable=randomData,
	relief=RIDGE,
	bd=3)
checkDataRandom.grid(
	row=0, 
	column=0, 
	padx=5, 
	pady=5, 
	sticky=W)

checkDataStairs = Checkbutton(
	UI_frame, 
	bg='#a7a7a7', 
	text='Stairs data', 
	font=font, 
	variable=stairsData,
	relief=RIDGE,
	bd=3)
checkDataStairs.grid(
	row=1, 
	column=0, 
	padx=5, 
	pady=5, 
	sticky=W)
checkDataStairs.select()

# buttons
Button(
	UI_frame, 
	text="Generate", 
	command=Generate, 
	bg='#15b4ea', 
	font=font,
	relief=RIDGE,
	bd=3,
	justify=RIGHT,
	).grid(row=2, column=4,columnspan=2, padx=5, pady=5, sticky=EW)

Button(
	algorithms_frame, 
	text="Bubble", 
	command=bubble, 
	bg='#ff0000', 
	font=font,
	relief=RIDGE,
	bd=3,
	justify=RIGHT,
	).grid(row=0, column=0, padx=5, pady=5)

Button(
	algorithms_frame, 
	text="Selection", 
	command=selection, 
	bg='#ffaa00', 
	font=font,
	relief=RIDGE,
	bd=3,
	justify=RIGHT,
	).grid(row=0, column=1, padx=5, pady=5, sticky=EW)

Button(
	algorithms_frame, 
	text="Bubble+", 
	command=bubblePlus, 
	bg='#ebf100', 
	font=font,
	relief=RIDGE,
	bd=3,
	justify=RIGHT,
	).grid(row=0, column=2, padx=5, pady=5)

Button(
	algorithms_frame, 
	text="Insertion", 
	command=insertion, 
	bg='#ebf100', 
	font=font,
	relief=RIDGE,
	bd=3,
	justify=RIGHT,
	).grid(row=0, column=3, padx=5, pady=5)

Button(
	algorithms_frame, 
	text="Coktail", 
	command=coktail, 
	bg='#d5ff00', 
	font=font,
	relief=RIDGE,
	bd=3,
	justify=RIGHT,
	).grid(row=0, column=4, padx=5, pady=5)

Button(
	algorithms_frame, 
	text="Merge", 
	command=merge, 
	bg='#80ff00', 
	font=font,
	relief=RIDGE,
	bd=3,
	justify=RIGHT,
	).grid(row=0, column=5, padx=5, pady=5)

Button(
	algorithms_frame, 
	text="Quick", 
	command=quick, 
	bg='#80ff00', 
	font=font,
	relief=RIDGE,
	bd=3,
	justify=RIGHT,
	).grid(row=0, column=6, padx=5, pady=5)

Button(
	algorithms_frame, 
	text="Bucket", 
	command=bucket, 
	bg='#00ff00', 
	font=font,
	relief=RIDGE,
	bd=3,
	justify=RIGHT,
	).grid(row=0, column=7, padx=5, pady=5)
root.mainloop()