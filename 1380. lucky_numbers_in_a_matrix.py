from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
        col = []
        for j in range(len(matrix[0])):
            cur = []
            for k in range(len(matrix)):
                # print("j, k, matrix[k][j]: ", j, k, matrix[k][j])
                cur.append(matrix[k][j])
            col.append(cur)
        # print("col: ", col)

        for i in range(len(matrix)):
            for l in range(len(matrix[0])):
                # print("i, l, cur: ", i, l, matrix[i][l])
                cur = matrix[i][l]
                if cur == min(matrix[i]) and cur == max(col[l]):
                    return [cur]

def main(matrix):
    result = Solution()
    print(result.luckyNumbers(matrix))

if __name__== "__main__" :
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    main(matrix)
