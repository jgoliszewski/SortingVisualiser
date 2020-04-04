from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.maxsize(900,600)
root.config(bg='black')

#variables
algorithms = ['Bubble Sort','Merge Sort']
selected_alg = StringVar()

def Generate():
	print(f"Selected algorithm: {selected_alg.get()}")


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
Button(UI_frame, text="Generate", command=Generate, bg='red').grid(row=0, column=2, padx=5, pady=5)

#Row[1]
Label(UI_frame, text='Size: ', bg='gray').grid(row=1, column=0, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5)

Label(UI_frame, text='Min Value ', bg='gray').grid(row=1, column=2, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5)

Label(UI_frame, text='Max Value: ', bg='gray').grid(row=1, column=4, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5)


root.mainloop()