'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashtable = {}
        
        for i in range(len(s)):
            if s[i] not in hashtable:
                hashtable[s[i]] = [i]
            else:
                hashtable[s[i]].append(i)
        
        for i in range(len(s)):
            if len(hashtable[s[i]]) == 1:
                return hashtable[s[i]][0]
            
        
        return -1