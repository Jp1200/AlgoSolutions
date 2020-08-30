def findThreeLargestNumbers(array):
	bigNums = [None, None, None]
    for num in array:
		UpdateArrayWithLargeNum(bigNums,num)
	return bigNums	
    
def UpdateArrayWithLargeNum(array,num):
	if array[2] is None or num > array[2]:
		shiftNum(array,num,2)
	elif array[1] is None or num >array[1]:
		shiftNum(array,num,1)
	elif array[0] is None or num > array[0]:
		shiftNum(array,num,0)
		
def shiftNum(array,num,index):
	for i in range(index+1):
		if i == index:
			array[i] = num
		else:
			array[i]= array[i+1]

# init an array of three none spots and then  for eevery num in array we check every postion in 
# the init'd array to see if its first bigger than the last spot, then the middle spot,
# then the first spot
# if it is then we shift positions so that the largest int is always the last position of the bigNum array
