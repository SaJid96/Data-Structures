
  Q~Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.
  
  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.


  You can assume that there will be at most one pair of numbers summing up to
  the target sum.

sample Input = [3, 5, -4, 8, 11, 1, -1, 6]

sample out put=[-1, 11] 

Time Complexty: O(n)
space Complexity:O(n)



#sol 1

def TwoNumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstNum=array[i]
        for j in range(i+1,len(array):
            secondNum=array[j]
            if firestNum+secindnum == targetSum
                return [firstnum,secondNum]

        return []


#sol 2

def TwoNumberSum(array,targetSum):
    nums={}
    for num in array:
        potential =targetSum-num
        if Potential in nums:
            return [potentialMatch,num]

        else:
        nums[num]=True

    return []

