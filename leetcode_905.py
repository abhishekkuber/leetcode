'''
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [0] * len(nums)
        start = 0
        end = len(nums)-1
        
        for i in nums:
            if i%2 == 0:
                output[start] = i
                start += 1
            else:
                output[end] = i
                end -= 1
        
        return output