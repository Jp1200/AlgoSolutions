def twoNumberSum(array, targetSum):
    for i in range(len(array)):
		currentNum = array[i]

		for j in range(i+1, len(array)):
			if array[j]+currentNum == targetSum:
				return [currentNum, array[j]]

	return []		
    pass
# Simple Solution O(n^2) Space time complexity as you have two loops which go through a single array 
def twoNumberSumHash(array, targetSum):
    hash = {}
    # init Hash to store numbers
	for x in array:
        # Math dictates that X+Y = Target
        # where then _>
		y = targetSum - x
		if y in hash: 
            # so if y is in the hash via this py function return the numbers
			return [y,x]
		else:
            # if it doesnt then store it as true 
			hash[x] = True
	return []	
    pass
# Hash Solution which has O(n) complexity wh
def twoNumberSum(array, targetSum):
    hash = {}
	for x in array:
		y = targetSum - x
		if y in hash:
			return [y,x]
		else:
			hash[x] = True
	return []	
    pass
def twoNumberSumSorted(array,targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum ==targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
# Sortiung the array first allows left to right checking by going through the lowest number
# and highest number checking if the far left number plus far right equals target and if its 
# less that target move left up one index because sum is too low
#  obviously the opposite for right side in elif statements






