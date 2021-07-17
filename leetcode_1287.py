'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
'''

class Solution(object):
    def findSpecialInteger(self, arr):
        for i in arr:
            if(arr.count(i) >= (len(arr)/4)+1):
                return i