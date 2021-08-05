'''
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashtable = {}
        
        for i in magazine:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1
        
        for j in ransomNote:
            if j not in hashtable:
                return False
            else:
                if hashtable[j] == 0:
                    return False
                else:
                    hashtable[j] -= 1
        
        return True
        
        