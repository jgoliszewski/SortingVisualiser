import time
green = '#00e30b'
orange = '#ffa500'

def bubbleSort(data, drawData, timeTick, sort, comprasions=0):
	for j in range(len(data)-1):
		for i in range(len(data)-1):
			drawData(data, [green if x in sort else 'red' for x in range(len(data))], False, i, comprasions=comprasions)
			comprasions += 1
			if data[i] > data[i+1]:
				swapBubble(data, i, i+1, sort, drawData, timeTick, comprasions)
				drawData(data, [green if x in sort else 'red' for x in range(len(data))], False, i, comprasions=comprasions)
				time.sleep(timeTick/2)
			else:
				time.sleep(timeTick)
			drawData(data, [green if x in sort else 'red' for x in range(len(data))], False, i, comprasions=comprasions)
		sort.append(len(data)-1-j)

def bubbleSortPlus(data, drawData, timeTick, sort, comprasions=0):
	swap = True
	for j in range(len(data)-1):
		if swap:
			swap = False
			for i in range(len(data)-j-1):
				drawData(data, [green if x in sort else 'red' for x in range(len(data))],False, i, comprasions=comprasions)
				comprasions += 1
				if data[i] > data[i+1]:
					swap = True
					swapBubble(data, i, i+1, sort, drawData, timeTick, comprasions)
					drawData(data, [green if x in sort else 'red' for x in range(len(data))],False, i, comprasions=comprasions)
					time.sleep(timeTick/2)
				else:
					time.sleep(timeTick)
					drawData(data, [green if x in sort else 'red' for x in range(len(data))],False, i, comprasions=comprasions)
			sort.append(len(data)-1-j)

def swapBubble(data, i, j, sort, drawData, timeTick, comprasions):
	colors = []
	for x in range(len(data)):
		if x == i or x == j:
			colors.append(orange)
		elif x in sort:
			colors.append(green)
		else:
			colors.append('red')
	time.sleep(timeTick/3)
	drawData(data, colors, False, i, comprasions=comprasions)
	data[i], data[j] = data[j], data[i]
	time.sleep(timeTick/2)
	drawData(data, colors, False, i, comprasions=comprasions)
	time.sleep(timeTick/3)

