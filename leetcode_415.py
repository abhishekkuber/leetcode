'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        idx = 0
        number1 = 0
        for i in (num1[::-1]):
            number1 += (ord(i) - 48) * (10 ** idx)
            idx += 1
        
        idx = 0
        number2 = 0
        for i in (num2[::-1]):
            number2 += (ord(i) - 48) * (10 ** idx)
            idx += 1

        return (str(number1 + number2))