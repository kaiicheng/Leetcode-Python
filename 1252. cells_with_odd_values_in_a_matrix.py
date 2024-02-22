from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        mat = [[0 for j in range(n)] for i in range(m)]
        # print("mat: ", mat)

        for i in range(len(indices)):
            r = indices[i][0]
            c = indices[i][1]
            for j in range(len(mat)):
                if j == r:
                    for k in range(len(mat[j])):
                        mat[j][k] += 1
            # print("mat: ", mat)
            for j in range(len(mat[0])):
                if j == c:
                    for k in range(len(mat)):
                        # print("k, j: ", k, j)
                        mat[k][j] += 1
            # print("mat: ", mat)

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] % 2 == 1:
                    ans += 1
        return ans

def main(m, n, indices):
    result = Solution()
    print(result.oddCells(m, n, indices))

if __name__== "__main__" :
    m = 2
    n = 3
    indices = [[0,1],[1,1]]
    main(m, n, indices)
