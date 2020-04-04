import time
green = '#00e30b'
def bubbleSort(data, drawData, timeTick):
	for _ in range(len(data)-1):
		for i in range(len(data)-1):
			drawData(data, [green if x == i or x == i+1 else 'red' for x in range(len(data))])
			if data[i] > data[i+1]:
				data[i], data[i+1] = data[i+1], data[i]
				time.sleep(timeTick/2)
				drawData(data, [green if x == i or x == i+1 else 'red' for x in range(len(data))])
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
				drawData(data, [green if x == i or x == i+1 or x in sort else 'red' for x in range(len(data))])
				if data[i] > data[i+1]:
					swap = True
					data[i], data[i+1] = data[i+1], data[i]
					time.sleep(timeTick/2)
					drawData(data, [green if x == i or x == i+1 or x in sort else 'red' for x in range(len(data))])
					time.sleep(timeTick/2)
				else:
					time.sleep(timeTick)
		sort.append(len(data)-j-1)
	drawData(data, [green for x in range(len(data))], finished=True)