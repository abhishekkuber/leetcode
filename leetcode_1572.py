'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
'''

class Solution(object):
    def diagonalSum(self, mat):
        total_sum = 0
        for i in range(len(mat)):
            total_sum += (mat[i][i] + mat[i][len(mat)-i-1])
            
        if len(mat)%2 != 0:
            mid = (len(mat)//2)
            total_sum -= mat[mid][mid]
        
        return total_sum 
                
        