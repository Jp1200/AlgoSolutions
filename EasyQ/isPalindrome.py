def isPalindrome(string):
	check = ""

	lengthStr = len(string)
	counter = 0
    while counter < lengthStr:
		check = check + string[lengthStr - counter - 1]
		counter += 1
	if check == string:
		return True
	else:
		return False
    
# O(n) time and O(n) space 

# Fastest way is to compare left index and right index at the same time:

def isPalindrome2(string):
    leftIndex = 0
    rightIndex = len(string) - 1
    while leftIndex < rightIndex:
        if string[leftIndex] != string[rightindex]:
            return False #as soon as the left and right index arnt the same it isnt a palindrome
        leftIndex += 1
        rightIndex += 1
    return True    
