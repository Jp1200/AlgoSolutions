def binarySearch(array, target):
    for num in array:
        print(num)
        if num == target:
            return array.index(num)

    return -1
