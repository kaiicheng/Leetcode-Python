from collections import Counter
from typing import List

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        # print("mat: ", mat)
        ls = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                # print("i, j: ", i, j)
                ls.append(mat[i][j])
        ls.sort()
        c = Counter(ls)
        ans = []
        for i in c:
            if c[i] >= len(mat):
                ans.append(i)
        ans.sort()
        # print("ans: ", ans)
        if len(ans) == 0:
            return -1
        else:
            return min(ans)
    
def main(mat):
    result = Solution()
    print(result.smallestCommonElement(mat))

if __name__== "__main__" :
    mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
    main(mat)
