# main diagonal iteration:
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# diagonal = [matrix[i][i] for i in range(len(matrix))]
# print("Main Diagonal:", diagonal)

# secondary diagonal iteration (for a square matrix):
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# secondary_diagonal = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
# print("Secondary Diagonal:", secondary_diagonal)

from typing import List

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        for i in range(len(grid)):
            
            # secondary diagonal iteration (for a square matrix):
            # print("grid[i][len(grid) - 1 - i]: ", grid[i][len(grid) - 1 - i])
            if grid[i][len(grid) - 1 - i] == 0:
                return False
            
            for j in range(len(grid[i])):
                # print("i, j, grid[i][j]: ", i, j, grid[i][j])
                # print("j, i, grid[j][i]: ", j, j, grid[j][i])
                if i == j:
                    if grid[i][j] == 0:
                        return False
                elif j != len(grid) - 1 - i:
                    if grid[i][j] != 0:
                        return False
        return True

def main(grid):
    result = Solution()
    print(result.checkXMatrix(grid))

if __name__== "__main__" :
    grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
    main(grid)
