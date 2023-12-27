from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print("i, j: ", i, j)
                if grid[i][j] < 0:
                    # print("grid[i]: ", grid[i])
                    count += 1
                    count += len(grid[i]) - j - 1
                    # print("count: ", count)
                    break
        return count

def main(grid):
    result = Solution()
    print(result.countNegatives(grid))

if __name__== "__main__" :
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    main(grid)
