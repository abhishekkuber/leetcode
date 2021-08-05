'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
'''

class Solution(object):
    def isValid(self, s):
        stack = []

        if (len(s)%2 != 0):
            return False
        else:
            for i in s:
                if(i == '[' or i=='{' or i=='('):
                    stack.append(i)
                elif(i == ']' and len(stack) != 0):
                    if stack[-1] == '[':
                        stack = stack[:-1]
                    else:
                        break
                elif(i == '}' and len(stack) != 0):
                    if stack[-1] == '{':
                        stack = stack[:-1]
                    else:
                        break
                elif(i == ')' and len(stack) != 0):
                    if stack[-1] == '(':
                        stack = stack[:-1]
                    else:
                        break
                else:
                    return False

            if (len(stack) == 0):
                return True