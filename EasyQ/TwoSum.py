def twoNumberSum(array, targetSum):
    for i in range(len(array)):
		currentNum = array[i]

		for j in range(i+1, len(array)):
			if array[j]+currentNum == targetSum:
				return [currentNum, array[j]]

	return []		
    pass
# Simple Solution O(n^2) Space time complexity as you have two loops which go through a single array 
