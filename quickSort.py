import time
green = '#00e30b'
orange = '#ffa500'
blue = '#15b4ea'
comp = 0

def quickSortBorder(data, head, tail, drawData, timeTick, sort, bucket=True, bucketColors=None):
	global comp
	border = head
	pivot = data[tail]
	
	for i in range(head, tail):
		colors = colorArray(data, i, sort, head, tail, bucket=bucket, bucketColors=bucketColors)
		drawData(data, colors, False, i, tail, border, comprasions=comp)
		time.sleep(timeTick/4)
		comp += 1

		if data[i] < pivot:

			swapQuick(data, i, border, sort, drawData, timeTick, tail, border, head, bucket=bucket, bucketColors=bucketColors)
			colors = colorArray(data, i, sort, head, tail, bucket=bucket, bucketColors=bucketColors)
			drawData(data, colors, False, i, tail, border, comprasions=comp)
			time.sleep(timeTick/4)
			border += 1
	
	swapQuick(data, tail, border, sort, drawData, timeTick, tail, border, head, True, bucket=bucket, bucketColors=bucketColors)
	sort.append(border)

	if abs(tail - head) == 1:
		sort.append(tail)

	colors = colorArray(data, i, sort, head, tail, bucket=bucket, bucketColors=bucketColors)
	drawData(data ,colors, False, -10, tail, border, comprasions=comp)
	time.sleep(timeTick/4)

	return border


def quickSort(data, head, tail, drawData, timeTick, sort, comprasions=None, bucket=False, bucketColors=None):
	global comp

	if comprasions != None:
		comp = comprasions

	if head < tail:
		border = quickSortBorder(data, head, tail, drawData, timeTick,sort, bucket=bucket, bucketColors=bucketColors)

		quickSort(data, head, border-1, drawData, timeTick, sort, bucket=bucket, bucketColors=bucketColors)

		quickSort(data, border+1, tail, drawData, timeTick, sort, bucket=bucket, bucketColors=bucketColors)

	else:
		sort.append(head)

	return comp

def swapQuick(data, i, j, sort, drawData, timeTick, tail, border, head, pivotSwaping=False, bucket=True, bucketColors=None):
	colors = colorArray(data, i, sort, head, tail, j, pivotSwaping=pivotSwaping, bucket=bucket, bucketColors=bucketColors)


	drawData(data, colors, False, i, tail, border, comprasions=comp)
	time.sleep(timeTick/4)
	data[i], data[j] = data[j], data[i]
	drawData(data, colors, False, i, tail, border, comprasions=comp)
	time.sleep(timeTick/4)

def colorArray(data, i, sort, head, tail, j=None, pivotSwaping=False, bucket=True, bucketColors=None):
	colors = []
	color = blue if pivotSwaping else 'red'

	for x in range(len(data)):

		if x in sort:
			if bucket:
				colors.append(bucketColors[x])

			else:
				colors.append(green)

		elif x < head or x > tail:
			if bucket:
				colors.append(bucketColors[x])

			else:
				colors.append('gray')

		elif x == i or x == j:
			colors.append(color)

		else:
			colors.append(orange)

	return colors
