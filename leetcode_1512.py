'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
'''

class Solution(object):
    def numIdenticalPairs(self, nums):
        total_elements = len(nums)
        count = 0
        for i in range(total_elements):
            for j in range(i+1, total_elements):
                if(nums[i] == nums[j]):
                    count = count + 1
        return count

