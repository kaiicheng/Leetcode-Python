from typing import List
from collections import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        mx = -1
        index = -1
        for i in range(len(mat)):
            # print(mat[i].count(1))
            if mat[i].count(1) > mx:
                mx = mat[i].count(1)
                index = i
        return [index, mx]

def main(mat):
    result = Solution()
    print(result.rowAndMaximumOnes(mat))

if __name__== "__main__" :
    mat = [[0,0,0],[0,1,1]]
    main(mat)
