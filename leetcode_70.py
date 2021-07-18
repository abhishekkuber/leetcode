'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


For each step, as the maximum number we can take is 2, we could have either come from the (n-1)th step or (n-2)th step, so add those 2

'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        f = []
        
        f.append(1)
        f.append(2)
        
        for i in range(2, n):
            f.append(f[i - 1] + f[i - 2])
            
        return f[n - 1]