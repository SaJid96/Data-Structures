
"""
 Write a function that takes in a non-empty array of integers that are sorted
   in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.?
"""
"""
time complexity : O(nlogn)
reason: we need to sort our output array
actually time complexity is O(n+nlogn) but since we are working with big O notation here we can remove this n because n is going to be less than n miltiplied by log n and so what if we assume  n is equal to nlog n we get something like 2 multiplied by n log n and two is obviously constant so we can remove the constant  and well taht leads us to time complexity of n log n

sol 1: we have additional  n step  , we need to genearte al the squares and put theose into an array and then after we generate all those squares of array we then need to sort the output array but since first step takes the much les time than the second step , whic is nlogn we can assume it takes the same amount time that gives constant two times n log n because  if we have n log n time + n log n time and then we will remove the  two cuz of big O notation

space complexity: O(n)
reason: beacuse we need to generate the brand ne structure


sol 2:we are going to intialize empty o/p array


optimal complexity:

time complexity & space complexity: O(n)

"""

# sol 1


def sortedSquaredArray(array):
    # Write your code here.
	sortedSquares=[0 for _ in array]
	
	for idx in range(len(array)):
		value=array[idx]
		sortedSquares[idx]=value * value
		
	sortedSquares.sort()
	return sortedSquares


# sol 2

def sortedSquaredArray(array):
    # Write your code here.
	sortedSquares=[0 for _ in array]
	smallerValueIdx=0
	largerValueIdx=len(array)-1
	
	for idx in reversed(range(len(array))):
		smallerValue=array[smallerValueIdx]
		largerValue=array[largerValueIdx]
		
		if abs(smallerValue) > abs(largerValue):
			sortedSquares[idx]=smallerValue * smallerValue
			
			smallerValueIdx +=1
		else:
			sortedSquares[idx]=largerValue * largerValue
			largerValueIdx -=1
   
    return sortedSquares 
