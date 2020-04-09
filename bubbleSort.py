import time
green = '#00e30b'
orange = '#ffa500'

def bubbleSort(data, drawData, timeTick, sort, comprasions=0):
	for j in range(len(data)-1):
		for i in range(len(data)-1):
			colors = colorArray(len(data), i, sort)
			drawData(data, colors, False, i, comprasions=comprasions)
			time.sleep(timeTick/3)
			comprasions += 1
			if data[i] > data[i+1]:
				swapBubble(data, i, i+1, sort, drawData, timeTick, comprasions)
				colors = colorArray(len(data), i+1, sort)
				drawData(data, colors, False, i+1, comprasions=comprasions)
				time.sleep(timeTick/6)
			else:
				time.sleep(timeTick/2)
		sort.append(len(data)-1-j)

def bubbleSortPlus(data, drawData, timeTick, sort, comprasions=0):
	swap = True
	for j in range(len(data)-1):
		if swap:
			swap = False
			for i in range(len(data)-j-1):
				colors = colorArray(len(data), i, sort)
				drawData(data, colors,False, i, comprasions=comprasions)
				time.sleep(timeTick/3)
				comprasions += 1
				if data[i] > data[i+1]:
					swap = True
					swapBubble(data, i, i+1, sort, drawData, timeTick, comprasions)
					colors = colorArray(len(data), i+1, sort)
					drawData(data, colors,False, i+1, comprasions=comprasions)
					time.sleep(timeTick/6)
				else:
					time.sleep(timeTick/2)
			sort.append(len(data)-1-j)

def swapBubble(data, i, j, sort, drawData, timeTick, comprasions):
	colors = colorArray(len(data), i, sort, j)

	drawData(data, colors, False, i, comprasions=comprasions)
	time.sleep(timeTick/4)
	data[i], data[j] = data[j], data[i]
	drawData(data, colors, False, j, comprasions=comprasions)
	time.sleep(timeTick/4)

def colorArray(lenData, i, sort, j=None):
	colors = []
	for x in range(lenData):
		if x in sort:
			colors.append(green)
		elif x == i or x == j:
			colors.append('red')
		else:
			colors.append(orange)
	return colors