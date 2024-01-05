from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        [[7,3,1,9],
         [3,4,6,9],
         [6,9,6,6],
         [9,5,8,5]]

        if len(mat) == 1:
            return sum(mat[0])

        ans = 0

        # primary diagonal
        for i in range(len(mat)):
            shift = 0
            for j in range(len(mat[i])):
                # print("i, j: ", i, j)
                # print("mat[j][i]: ", mat[j][i])
                # print("mat[j][i + shift]: ", mat[j][i + shift])
                ans += mat[j][i + shift]
                shift += 1
                # print("ans: ", ans)
            break

        # print("---primary above and secondary below---")

        # secondary diagonal
        for i in range(len(mat) - 1, -1, -1):
            # print("i: ", i)
            shift = 0
            for j in range(len(mat[i])):
                # print("i, j: ", i, j)
                # print("mat[j][i]: ", mat[j][i])
                # print("mat[j][i - shift]: ", mat[j][i - shift])
                ans += mat[j][i - shift]
                shift += 1
                # print("ans: ", ans)
            break
        
        if len(mat) % 2 != 0:
            # print("minus!")
            ans -= mat[len(mat) // 2][len(mat[0]) // 2]

        return ans

def main(mat):
    result = Solution()
    print(result.diagonalSum(mat))

if __name__== "__main__" :
    mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    main(mat)
