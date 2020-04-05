import time
green = '#00e30b'
def bubbleSort(data, drawData, timeTick, sort):
	for j in range(len(data)-1):
		for i in range(len(data)-1):
			drawData(data, [green if x in sort else 'red' for x in range(len(data))], False, i)
			if data[i] > data[i+1]:
				swapBubble(data, i, i+1, sort, drawData, timeTick)
				drawData(data, [green if x in sort else 'red' for x in range(len(data))], False, i)
				time.sleep(timeTick/2)
			else:
				time.sleep(timeTick)
			drawData(data, [green if x in sort else 'red' for x in range(len(data))], False, i)
		sort.append(len(data)-1-j)

def bubbleSortPlus(data, drawData, timeTick, sort):
	swap = True
	for j in range(len(data)-1):
		if swap:
			swap = False
			for i in range(len(data)-j-1):
				drawData(data, [green if x in sort else 'red' for x in range(len(data))],False, i)
				if data[i] > data[i+1]:
					swap = True
					swapBubble(data, i, i+1, sort, drawData, timeTick)
					
					drawData(data, [green if x in sort else 'red' for x in range(len(data))],False, i)
					time.sleep(timeTick/2)
				else:
					time.sleep(timeTick)
			sort.append(len(data)-1-j)

def swapBubble(data, i, j, sort, drawData, timeTick):
	colors = []
	for x in range(len(data)):
		if x == i or x == j:
			colors.append('orange')
		elif x in sort:
			colors.append(green)
		else:
			colors.append('red')
	time.sleep(timeTick/3)
	drawData(data, colors, False, i)
	data[i], data[i+1] = data[i+1], data[i]
	time.sleep(timeTick/2)
	drawData(data, colors, False, i)
	time.sleep(timeTick/3)

def quickSortBorder(data, head, tail, drawData, timeTick, sort):
	border = head
	pivot = data[tail]
	for i in range(head, tail):
		drawData(data,[green if x in sort else 'red' for x in range(len(data))], False, i, tail, border)
		time.sleep(timeTick/2)
		if data[i] < pivot:
			swapQuick(data, i, border, sort, drawData, timeTick, tail, border)
			drawData(data,[green if x in sort else 'red' for x in range(len(data))], False, i, tail, border)
			time.sleep(timeTick/2)
			border += 1
	
	swapQuick(data, tail, border, sort, drawData, timeTick, tail, border, True)
	sort.append(border)
	if abs(tail - head) == 1:
		sort.append(tail)

	drawData(data,[green if x in sort else 'red' for x in range(len(data))], False, -10, tail, border)
	time.sleep(timeTick/2)

	return border


def quickSort(data, head, tail, drawData, timeTick, sort):
	if head < tail:
		border = quickSortBorder(data, head, tail, drawData, timeTick,sort)

		quickSort(data, head, border-1, drawData, timeTick, sort)
		quickSort(data, border+1, tail, drawData, timeTick, sort)

def swapQuick(data, i, j, sort, drawData, timeTick, tail, border, pivotSwaping=False):
	colors = []
	color = '#15b4ea' if pivotSwaping else 'orange'

	for x in range(len(data)):
		if x in sort:
			colors.append(green)
		elif x == i or x == j:
			colors.append(color)
		else:
			colors.append('red')

	drawData(data, colors, False, i, tail, border)
	time.sleep(timeTick/2)
	data[i], data[j] = data[j], data[i]
	drawData(data, colors, False, i, tail, border)
	time.sleep(timeTick/2)
