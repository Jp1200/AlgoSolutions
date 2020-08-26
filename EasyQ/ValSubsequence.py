def isValidSubsequence(array, sequence):
	aInx = 0
	sInx = 0
	while aInx < len(array) and sInx < len(sequence):
		if array[aInx] == sequence[sInx]:
			sInx += 1
		aInx += 1
    return sInx == len(sequence)
# init indexs and then if val in  array is  the sequence val increase
# sequence index because then we want to check ifthe next value matchs in array
# increase array index 
