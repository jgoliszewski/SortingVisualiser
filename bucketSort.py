import time 
from quickSort import quickSort

comp = 0
orange = '#ffa500'
colorSet = ['#bffcc6','#fff5ba','#ffbebc','#ff9cee','#d5aaff','#85e3ff','#c4faf8','#98fb98']
#colorSet = ['black','red','orange','blue','green','brown','purple','yellow']

def bucketSort(data, drawData, timeTick,):
	global comp
	comp = 0
	data2 = []
	colors = []

	if len(data) >= 32:
		for i in range(8):
			data2.append([])

	else:
		for i in range(5):
			data2.append([])

	x = max(data) // len(data2) + 1 
	for i in range(len(data)):
		comp += 1
		idx = data[i] // x

		colors.append(colorSet[idx])
		data2[idx].append(data[i])
		color = colorArray(len(data), colors)
		drawData(data, color, finished=False, comprasions=comp, pointer=i)
		time.sleep(timeTick/4)

	data.clear()
	colors.clear()

	for i, d in enumerate(data2):
		for x in d:
			data.append(x)
			colors.append(colorSet[i])

	time.sleep(timeTick/4)
	drawData(data, colors, finished=False, comprasions=comp)
	time.sleep(timeTick/4)

	l = 0
	for i in range(len(data2)):
		r = l+len(data2[i])
		comp = quickSort(data, l, r-1, drawData, timeTick, sort=[], comprasions=comp, bucket=True, bucketColors=colors)

		drawData(data, colors, finished=False, comprasions=comp)

		l += len(data2[i])
		if i == len(data):
			comp = getComp()


def colorArray(lenData, colorData):
	colors = []
	
	for i in range(lenData):

		try:
			colors.append(colorData[i])

		except:
			colors.append(orange)

	return colors

