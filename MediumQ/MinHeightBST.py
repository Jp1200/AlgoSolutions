def minHeightBst(array):
	return construction(array, 0, len(array) - 1)

# recursive approach
#  start index starts at 0 and end starts at -1 of array
# the middle is, if even, the left of the middle, if odd
# simply the middle index
# Root node is intialized with middle index 
# because the array is already sorted the construction of the bst 
# is easy since we know which index is having the smallest index
# all starting indexs will be less than the root node 
# so the bst.left value is going to organize the left half of the array
# and the right half will be the other end 

def construction(array, startI, endI):
	if endI < startI:
		return None
	midI = (startI + endI) // 2
	bst = BST(array[midI])
	bst.left = construction(array, startI, midI -1) #  start never changes and the end is the middle -1 index
	bst.right = construction(array, midI + 1, endI) # end never moves but the start is one further than the middle index
	return bst

# We keep recursivly creating the bst until the array has been fully scraped


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
