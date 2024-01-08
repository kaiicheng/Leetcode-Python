from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        old_sum = 0
        for i in range(len(grid)):
            old_sum += sum(grid[i])
        # print("old_sum: ", old_sum)
        
        col = []
        row = []
        # row = [i for i in grid]  # need to use deepcopy
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[i])):
                temp.append(grid[i][j])
            row.append(temp)
            temp = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[i])):
                temp.append(grid[j][i])
            col.append(temp)
            temp = []
        # print("col: ", col)
        # print("row: ", row)

        # new_grid = []
        # for i in range

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print("i, j: ", i, j)
                # print("col: ", col)
                # print("row: ", row)
                
                cur_row = row[i]
                cur_col = col[j]
                # print("cur_row, cur_col: ", cur_row, cur_col)
                if grid[i][j] == max(cur_row) or grid[i][j] == max(cur_col):
                    pass
                else:
                    cur_row = cur_row[:j] + cur_row[j + 1: ]
                    cur_col = cur_col[:i] + cur_col[i + 1: ]
                    # print("cur_row, cur_col: ", cur_row, cur_col)

                    grid[i][j] = min(max(cur_row), max(cur_col))
                # print("grid: ", grid)
                # print("---end of iteration---")
        # print("grid: ", grid)

        new_sum = 0
        for i in range(len(grid)):
            new_sum += sum(grid[i])
        # print("new_sum: ", new_sum)
        
        return new_sum - old_sum

def main(grid):
    result = Solution()
    print(result.maxIncreaseKeepingSkyline(grid))

if __name__== "__main__" :
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    main(grid)
