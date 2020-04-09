import time
green = '#00e30b'
orange = '#ffa500'

def insertionSort(data, drawData, timeTick, comprasions=0):
	for j in range(len(data)):
		idx = j
		for i in range(j-1, -1, -1):
			colors = colorArray(len(data), idx, j)
			drawData(data, colors, pointer=idx, comprasions=comprasions)
			comprasions += 1
			if data[idx] < data[i]:
				swap(data, idx, i, j, drawData, timeTick, comprasions)
				idx -= 1
				colors = colorArray(len(data), idx, j)
				drawData(data, colors, pointer=idx, comprasions=comprasions)
				time.sleep(timeTick/3)
				drawData(data, colors, pointer=idx, comprasions=comprasions)
			else:
				time.sleep(timeTick/4)



def swap(data, i, j, k, drawData, timeTick, comprasions):

	colors = colorArray(len(data), i, k, j)

	time.sleep(timeTick/3)
	drawData(data, colors, False, i, comprasions=comprasions)
	data[i], data[j] = data[j], data[i]
	time.sleep(timeTick/3)
	drawData(data, colors, False, i, comprasions=comprasions)


def colorArray(lenData,idx, j, i=None):
	colors = []
	for x in range(lenData):
		if x == idx or x ==i:
			colors.append("red")
		elif x >j:
			colors.append("gray")
		else:
			colors.append(orange)
	return colors