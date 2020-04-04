from tkinter import *
from tkinter import ttk
import random
from sortingAlgorithms import bubbleSort


root = Tk()
root.title('Sorting Algorithm Visualiser')
root.maxsize(900,600)
root.config(bg='black')

#variables
algorithms = ['Bubble Sort','Merge Sort']
selected_alg = StringVar()
data = []

#functions
def drawData(data, colorArray):
	canvas.delete('all')
	canvas_height = 380
	canvas_width = 600
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
	bubbleSort(data, drawData, speedScale.get())





#frame loyout
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface
#Row[0]
Label(UI_frame, text='Algorithm: ', bg='gray').grid(row=0, column=0, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=[alg for alg in algorithms])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0,length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label='Select speed')
speedScale.grid(row=0, column=2, padx=5, pady=5)

Button(UI_frame, text="Start", command=startAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]

sizeEntry = Scale(UI_frame, from_=5, to=40, orient=HORIZONTAL, label='Data size')
sizeEntry.grid(row=1, column=0, padx=5, pady=5)


minEntry = Scale(UI_frame, from_=0, to=10, orient=HORIZONTAL, label='Min Value')
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, orient=HORIZONTAL, label='Max Value')
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()