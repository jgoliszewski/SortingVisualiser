import time
orange = '#ffa500'
comp = 0

def mergeSort(data, drawData, timeTick, maxValue, comprasions=None):
	global comp
	if comprasions == 0:
		comp = comprasions
	mergeSortAlg(data,0, len(data)-1, drawData, timeTick, maxValue)

def mergeSortAlg(data, left, right, drawData, timeTick, maxValue):
	if left < right:
		mid = (left + right) // 2

		mergeSortAlg(data, left, mid, drawData, timeTick, maxValue)
		mergeSortAlg(data, mid+1, right, drawData, timeTick, maxValue)
		merge(data, left, mid, right, drawData, timeTick, maxValue)

def merge(data, left, mid, right, drawData, timeTick, maxValue):
	global comp
	drawData(data, [orange if x >= left and x <= right else 'gray' for x in range(len(data))], maxValue=maxValue, comprasions=comp)
	time.sleep(timeTick/4)

	leftData = data[left:mid+1]
	rightData = data[mid+1:right+1]
	leftIdx = rightIdx = 0

	for idx in range(left, right+1):
		if leftIdx < len(leftData) and rightIdx < len(rightData):
			comp += 1
			if leftData[leftIdx] <= rightData[rightIdx]:
				data[idx] = leftData[leftIdx]
				leftIdx += 1

			else:
				data[idx] = rightData[rightIdx]
				rightIdx += 1
			drawData(data, [orange if x >= left and x <= right else 'gray' for x in range(len(data))], maxValue=maxValue, comprasions=comp)
			time.sleep(timeTick/4)

		elif leftIdx < len(leftData):
			data[idx] = leftData[leftIdx]
			leftIdx += 1

		else:
			data[idx] = rightData[rightIdx]
			rightIdx += 1
		drawData(data, [orange if x >= left and x <= right else 'gray' for x in range(len(data))], maxValue=maxValue, comprasions=comp)
		time.sleep(timeTick/4)
	drawData(data, [orange if x >= left and x <= right else 'gray' for x in range(len(data))], maxValue=maxValue, comprasions=comp)
	time.sleep(timeTick/6)
