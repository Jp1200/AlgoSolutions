def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pointer1 = 0
    pointer2 = 0
    current = float("inf")
    smallest = float("inf")
    smallestPair = []
       while (pointer1 < len(arrayOne)) and (pointer2 < len(arrayTwo)):
            num1 = arrayOne[pointer1]
            num2 = arrayTwo[pointer2]
            diff = abs(num1-num2)
            if diff == 0:
                return [num1, num2]
            elif num1 < num2:
                current = num2 - num1
                pointer1 += 1
            elif num2 < num1:
                current = num1 - num2
                pointer2 += 1
            else:
                return [num1, num2]
            if smallest > current:
                smallest = current
                smallestPair = [num1, num2]
        return smallestPair
