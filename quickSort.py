import time
green = '#00e30b'
orange = '#ffa500'

comp = 0

def quickSortBorder(data, head, tail, drawData, timeTick, sort):
	global comp
	border = head
	pivot = data[tail]
	for i in range(head, tail):
		drawData(data,[green if x in sort else orange for x in range(len(data))], False, i, tail, border, comprasions=comp)
		time.sleep(timeTick/2)
		comp += 1
		if data[i] < pivot:
			swapQuick(data, i, border, sort, drawData, timeTick, tail, border)
			drawData(data,[green if x in sort else orange for x in range(len(data))], False, i, tail, border, comprasions=comp)
			time.sleep(timeTick/2)
			border += 1
	
	swapQuick(data, tail, border, sort, drawData, timeTick, tail, border, True)
	sort.append(border)
	if abs(tail - head) == 1:
		sort.append(tail)

	drawData(data,[green if x in sort else orange for x in range(len(data))], False, -10, tail, border, comprasions=comp)
	time.sleep(timeTick/2)

	return border


def quickSort(data, head, tail, drawData, timeTick, sort, comprasions=None):
	global comp
	if comprasions == 0:
		comp = comprasions

	if head < tail:
		border = quickSortBorder(data, head, tail, drawData, timeTick,sort)

		quickSort(data, head, border-1, drawData, timeTick, sort)

		quickSort(data, border+1, tail, drawData, timeTick, sort)

def swapQuick(data, i, j, sort, drawData, timeTick, tail, border, pivotSwaping=False):
	colors = []
	color = '#15b4ea' if pivotSwaping else 'red'

	for x in range(len(data)):
		if x in sort:
			colors.append(green)
		elif x == i or x == j:
			colors.append(color)
		else:
			colors.append(orange)

	drawData(data, colors, False, i, tail, border, comprasions=comp)
	time.sleep(timeTick/2)
	data[i], data[j] = data[j], data[i]
	drawData(data, colors, False, i, tail, border, comprasions=comp)
	time.sleep(timeTick/2)