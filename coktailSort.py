import time 
green = '#00e30b'
orange = '#ffa500'

def coktailSort(data, drawData, timeTick, sort, comprasions=0):
	left = 0
	right = len(data)
	k = 0
	swaped = True
	for i in range(len(data)//2+1):
		if swaped:
			if swaped:
				swaped = False
				while k < right-1-i:
					colors = colorArray(len(data), k, sort)
					drawData(data, colors, False, k, comprasions=comprasions)
					time.sleep(timeTick/2)
					comprasions += 1
					if data[k] > data[k+1]:
						swap(data, k, k+1, sort, drawData, timeTick, comprasions)
						swaped = True
					k += 1
			sort.append(len(data)-i-1)
			k -= 1
			if swaped:
				swaped = False
				while k > left+i:
					colors = colorArray(len(data), k, sort)
					drawData(data, colors, False, k, comprasions=comprasions)
					time.sleep(timeTick/2)
					comprasions += 1
					if data[k] < data[k-1]:
						swap(data, k, k-1, sort, drawData, timeTick, comprasions)
						swaped = True
					k -= 1
			sort.append(i)
			k += 1



def swap(data, i, j, sort, drawData, timeTick, comprasions):
	colors = colorArray(len(data), i, sort, j)

	drawData(data, colors, False, i, comprasions=comprasions)
	time.sleep(timeTick/4)
	data[i], data[j] = data[j], data[i]
	drawData(data, colors, False, j, comprasions=comprasions)
	time.sleep(timeTick/4)


def colorArray(lenData, pointer, sort, i=None):
	colors = []

	for x in range(lenData):

		if x == pointer or x == i:
			colors.append('red')

		elif x in sort:
			colors.append(green)

		else:
			colors.append(orange)

	return colors