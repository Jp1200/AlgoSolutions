def selectionSort(array):
	currentInx = 0
	while currentInx < len(array) - 1:
		min_index = currentInx
    	for j in range(currentInx + 1, len(array)):
			if array[min_index] > array[j]:
				min_index = j
		swap(currentInx, min_index, array)
		currentInx += 1	
	return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Selction sort goes through a sub array and finds the min value and puts it in front 
# compares last int to every other int and swaps index if it finds something 
