import time
green = '#00e30b'
def bubbleSort(data, drawData, timeTick):
	for _ in range(len(data)-1):
		for i in range(len(data)-1):
			drawData(data, [green if x == i or x == i+1 else 'red' for x in range(len(data))], False, i)
			if data[i] > data[i+1]:
				data[i], data[i+1] = data[i+1], data[i]
				time.sleep(timeTick/2)
				drawData(data, [green if x == i or x == i+1 else 'red' for x in range(len(data))], False, i)
				time.sleep(timeTick/2)
			else:
				time.sleep(timeTick)
	drawData(data, ['#00e30b' for x in range(len(data))], finished=True)

def bubbleSortPlus(data, drawData, timeTick):
	swap = True
	sort = []
	for j in range(len(data)-1):
		if swap:
			swap = False
			for i in range(len(data)-j-1):
				drawData(data, [green if x == i or x == i+1 or x in sort else 'red' for x in range(len(data))],False, i)
				if data[i] > data[i+1]:
					swap = True
					data[i], data[i+1] = data[i+1], data[i]
					time.sleep(timeTick/2)
					drawData(data, [green if x == i or x == i+1 or x in sort else 'red' for x in range(len(data))],False, i)
					time.sleep(timeTick/2)
				else:
					time.sleep(timeTick)
		sort.append(len(data)-j-1)
	drawData(data, [green for x in range(len(data))], finished=True)


def quickSortBorder(data, head, tail, drawData, timeTick, sort):
	border = head
	pivot = data[tail]
	for i in range(head, tail):
		drawData(data,[green if x in sort else 'red' for x in range(len(data))], False, i, tail, border)
		time.sleep(timeTick/2)
		if data[i] < pivot:
			swap(data, i, border, sort, tail, border, drawData, timeTick)
			drawData(data,[green if x in sort else 'red' for x in range(len(data))], False, i, tail, border)
			time.sleep(timeTick/2)
			border += 1
	
	swap(data, tail, border, sort, tail, border, drawData, timeTick, True)
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

def swap(data, i, j, sort, tail, border, drawData, timeTick,pivotSwaping=False):
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
