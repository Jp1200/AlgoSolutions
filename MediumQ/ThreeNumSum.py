def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        leftindex = i + 1
        rightindex = len(array) - 1
        while leftindex < rightindex:
            currentSum = array[i] + array[leftindex] + array[rightindex]
            if currentSum == targetSum:
                triplets.append(
                    [array[i], array[leftindex], array[rightindex]])
                leftindex += 1
                rightindex -= 1
            elif (array[i] + array[leftindex] + array[rightindex]) < targetSum:
                leftindex += 1
            elif (array[i] + array[leftindex] + array[rightindex]) > targetSum:
                rightindex -= 1
    return triplets


# when you sort the array you know that the array has a form of
# [small# --------> large#] and setting points that move one space ahead and back from both ends of the array
# will potentially find the target sum and if the current sum is smaller than the
# target sum we can increase the left point because then our current sum will increase by nature of the sort
# this is likewise if currentSum is greater than target so we move right place to the left
# Optimal space time complexity is O(n^2) and space of O(n)
arr = [3, -2, 5, 8, 12, 4, -4, -2, 8]
print(threeNumberSum(arr, 7))
