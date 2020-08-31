def isMonotonic(array):
    if len(array) <= 2:
		return True

	direction = array[1] - array[0]
	for i in range(2,len(array)):
		
		if direction == 0:
			direction = array[i] - array[i-1]
			continue
		if breaks(direction,array[i-1],array[i]):
			return False
    return True
def breaks(direction,prev,curr):
	diff = curr - prev
	if direction > 0:
		return diff < 0
	return diff > 0
