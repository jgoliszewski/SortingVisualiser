from tkinter import *
from tkinter import ttk
import random
from sortingAlgorithms import bubbleSort, bubbleSortPlus, quickSort

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.maxsize(900,600)
root.config(bg='#b3b3b3')


#variables
algorithms = [
	'Bubble Sort',
	'Bubble Sort Plus',
	'Quick Sort']
selected_alg = StringVar()
data = []
font = ('Arial',15)

green = '#00e30b'
orange = '#ffa500'
#functions
def drawData(data, colorArray, finished=False, pointer=-10, pivot=None, border=None):
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
		y0 = canvas_height - height * 320
		#bottom right
		x1 = (i + 1) * x_width + offset
		y1 = canvas_height

		xp = pointer * x_width + offset + spacing
		canvas.create_text(xp+x_width/2-30, 23, anchor=SW, text='Pointer',font=font)
		canvas.create_rectangle(x0, y0, x1, y1, fill=['#15b4ea' if i == pivot else colorArray[i]])
		canvas.create_text(x0+x_width/2-10, y0, anchor=SW, text=str(data[i]),font=font)
	if pivot != None and border != None:
		xp = pivot * x_width + offset + spacing
		xb = border * x_width + offset + spacing
		yp = canvas_height - normalizedData[pivot] * 320
		canvas.create_text(xp+x_width/2-25, yp-30 if yp > 240 else yp + 30, anchor=SW, text='Pivot',font=font)
		canvas.create_text(xb+x_width/2-30, 42, anchor=SW, text='Border',font=font)


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

	if selected_alg.get() == "Quick Sort":
		quickSort(data, 0, len(data)-1, drawData, speedScale.get(),[])
		drawData(data, [green for x in range(len(data))], finished=True)
#frame loyout
UI_frame = Frame(root, 
	width=800, 
	height=200, 
	bg='#a7a7a7')
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
algMenu.current(2)

speedScale = Scale(UI_frame,
				from_=0.1,
				to=2.0,
				length=150,
				digits=2, 
				resolution=0.1,
				orient=HORIZONTAL, 
				label='Select Delay [s]',
				font=font,
				relief='groove',
				bg='white',
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
	bg='white',
	highlightbackground='black')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, 
	from_=0, 
	to=10, 
	orient=HORIZONTAL, 
	label='Min Value',
	font=font,
	bg='white',
	highlightbackground='black')
minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=E)

maxEntry = Scale(UI_frame, 
	from_=10, 
	to=100, 
	orient=HORIZONTAL, 
	label='Max Value',
	font=font,
	bg='white',
	highlightbackground='black')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, 
	text="Generate", 
	command=Generate, 
	bg='#15b4ea', 
	font=font
	).grid(row=1, column=3, padx=5, pady=5)

root.mainloop()