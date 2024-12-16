# Given an unsorted array arr[]. 
#Rotate the array to the left (counter-clockwise direction) 
#by d steps, where d is a positive integer. Do the mentioned 
#change in the array in place.

# Note: Consider the array as circular.

# Examples :

# Input: arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]
# Explanation: when rotated by 2 elements, 
#it becomes 3 4 5 1 2.

def rotateArr( arr, d):
    
   times=d%len(arr)
   new=arr[times:len(arr)]+arr[0:times]
        
   return new
        
print(rotateArr( [1,2,3,4,5], 2))