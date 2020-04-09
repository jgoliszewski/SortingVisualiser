import time
green = '#00e30b'
orange = '#ffa500'

def selectionSort(data, drawData, timeTick, sort=[], comprasions=0,):
	for j in range(len(data)):
		minIdx = j
		
		for i in range(j, len(data)):

			colors = colorArray(len(data), minIdx, sort)
			drawData(data, colors, False, i, comprasions=comprasions)
			comprasions += 1

			if data[i] < data[minIdx]:
				minIdx = i

			colors = colorArray(len(data), minIdx, sort)
			drawData(data, colors, False, i, comprasions=comprasions)
			time.sleep(timeTick)

		swap(data, minIdx, j, sort, i, drawData, timeTick, comprasions=comprasions)
		sort.append(j)

def swap(data, i, j, sort, pointer, drawData, timeTick, comprasions):
	colors = colorArray(len(data), i, sort, j)

	drawData(data, colors, False, pointer, comprasions=comprasions)
	time.sleep(timeTick/4)

	data[i], data[j] = data[j], data[i]
	
	drawData(data, colors, False, pointer, comprasions=comprasions)
	time.sleep(timeTick/4)

def colorArray(lenData, idx, sort, i=None):
	colors = []

	for x in range(lenData):

		if x == idx or x == i:
			colors.append("red")

		elif x in sort:
			colors.append(green)

		else:
			colors.append(orange)

	return colors