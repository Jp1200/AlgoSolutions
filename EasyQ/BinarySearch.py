def binarySearch(array, target):
    for num in array:
        print(num)
        if num == target:
            return array.index(num)

    return -1
# Not a binary serach algorithm but accomplishes the same goal but worst space time complexity


def binarySearch2(array, target):
    return binarySearchHelp(array, target, 0, len(array)-1)


def binarySearchHelp(array, target, left, right):
    while left <= right:
        middle = (left+right)//2
        potMatch = array[middle]
        if target == potMatch:
            return middle
        elif target < potMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1
#  I remeber from 1320 CS class that binary search starts in the middle of the array because it is assumed to be sorted:
#  so the middle index of the array is the target we are done adn return the middle int
#

# [left # # # # target # # middle # # # # # # # # right]
#  if the target int is less than the middle int we move the right index towards the left
#  now we have a new middle which should be closer to the target bc it is less tahn the prev middle int
#  [left # # # # target # middle # # # # # # # # right #]
