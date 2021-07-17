'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
'''

class Solution(object):
    def majorityElement(self, nums):
        unique = []
        for i in nums:
            if i not in unique:
                unique.append(i)
            
            
        finalAns = []
        for i in unique:
            if(nums.count(i) > len(nums)/3 ):
                finalAns.append(i)
        return finalAns