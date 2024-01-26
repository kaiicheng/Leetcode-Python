from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        n_soldier_row = []
        for i in range(len(mat)):
            n_soldier_row.append([mat[i].count(1), i])
        n_soldier_row.sort()
        # print("n_soldier_row: ", n_soldier_row)

        ans = []
        for i in range(k):
            ans.append(n_soldier_row[i][1])
        return ans

def main(mat, k):
    result = Solution()
    print(result.kWeakestRows(mat, k))

if __name__== "__main__" :
    mat = [[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], 
    k = 3
    main(mat, k)
