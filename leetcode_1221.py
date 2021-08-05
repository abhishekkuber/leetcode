'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
'''

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        stack = []
        
        for i in s:
            if i == 'L':
                if len(stack) > 0:
                    if stack[-1] == 'R':
                        stack.pop(-1)
                        if len(stack) == 0:
                            count += 1
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
                    
            else:
                if len(stack) > 0:
                    if stack[-1] == 'L':
                        stack.pop(-1)
                        if len(stack) == 0:
                            count += 1
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
                    
                    
        return count 
         