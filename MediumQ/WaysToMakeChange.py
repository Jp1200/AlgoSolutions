def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)]
	ways[0] = 1
	
	for denom in denoms:
		for amount in range(1,n+1):
			if denom <= amount:
				ways[amount] += ways[amount - denom]
				print(ways)
	return ways[n]
    
# Init an array of ways to make change which is n+1
# the zeroth position is the number of ways you can make 0 
#  which is 1 way where you have no coins
# for each denomination in the denoms array we check to see if 
# an amount (1,2,3,4,5,...n) is greater than or equal to the denomination
# If it is, then we take the ways for that amount add it to the previous number of ways
# and subtract the denom from the amount in the ways array
# so  if n = 2:
# ways = [1,0,0]
# denoms= [1,2]

# 1 <= 1 is true:
# => ways[1] = ways[1] + ways[1-1]
# => ways[1] + ways[0] = 1 since ways[0] = 1
# NOW ways = [1,1,0]
# Next => 1<=2 is true so:
# ways[2] + ways[2 - 1] = 0 + 1:
# => ways = [1,1,1]
#  now we do next denom
# => 2<= 1 is false so next:
# 2<=2 is true so:
# => ways[2] = ways[2] + ways[2-2] = 1 + 1 = 2

# Then the end of the array is the number of ways to make that amount with those denoms
# SO there are two ways to get 2 from denoms [1,2]
# 1x2 and 2x1