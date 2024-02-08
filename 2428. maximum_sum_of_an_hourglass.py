from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        ans = []

        for i in range(len(grid)):
            if i + 2 + 1 <= len(grid):

                # print("i, grid[i]: ", i, grid[i])
                # print("i + 1, grid[i + 1]: ", i + 1, grid[i + 1])
                # print("i + 2, grid[i + 2]: ", i + 2, grid[i + 2])

                for j in range(len(grid[i])):
                    if j + 2 + 1 <= len(grid[i]):
                        # print("j, grid[i][j]: ", j, grid[i][j])
                        cur = 0

                        for k in range(3):
                            # print("grid[i][j + k]: ", grid[i][j + k])
                            cur += grid[i][j + k]

                        
                        for k in range(3):
                            # print("grid[i + 2][j + k]: ", grid[i + 2][j + k])
                            cur += grid[i + 2][j + k]

                        for k in range(3):
                            if k == 1:
                                # print("grid[i + 1][j + k]: ", grid[i + 1][j + k])
                                cur += grid[i + 1][j + k]

                        # print("cur: ", cur)
                        ans.append(cur)

        # print("ans: ", ans)
        return max(ans)

def main(grid):
    result = Solution()
    print(result.maxSum(grid))

if __name__== "__main__" :
    grid = [[520626,685427,788912,800638,717251,683428],
            [23602,608915,697585,957500,154778,209236],
            [287585,588801,818234,73530,939116,252369]]
    main(grid)
