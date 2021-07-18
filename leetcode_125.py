'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s  = s.replace(' ', '')
        s = s.lower()
        x = ''.join(i for i in s if i.isalnum())
        
        string_list = list(x)
        
        if string_list == string_list[::-1]:
            return True
        else:
            return False