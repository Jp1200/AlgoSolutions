def bubbleSort(array):
    n = len(array)
    # print(n)
    # for index in range(n):
    # 	for j in range(0,n-index-1):
    # 		if array[j]> array[j+1]:
    # 			array[j+1], array[j] = array[j], array[j+1]
    # 	return array
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(n-1-counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
