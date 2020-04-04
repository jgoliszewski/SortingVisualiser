import time

def bubbleSort(data, drawData, timeTick):
	for _ in range(len(data)-1):
		for i in range(len(data)-1):
			if data[i] > data[i+1]:
				drawData(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))])
				data[i], data[i+1] = data[i+1], data[i]
				time.sleep(timeTick/2)
				drawData(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))])
				time.sleep(timeTick/2)
			else:
				drawData(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))])
				time.sleep(timeTick)
	drawData(data, ['green' for x in range(len(data))])

def bubbleSortPlus(data, drawData, timeTick):
	swap = True
	for j in range(len(data)-1):
		if swap:
			swap = False
			for i in range(len(data)-j-1):
				if data[i] > data[i+1]:
					swap = True
					drawData(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))])
					data[i], data[i+1] = data[i+1], data[i]
					time.sleep(timeTick/2)
					drawData(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))])
					time.sleep(timeTick/2)
				else:
					drawData(data, ['green' if x == i or x == i+1 else 'red' for x in range(len(data))])
					time.sleep(timeTick)

	drawData(data, ['green' for x in range(len(data))])