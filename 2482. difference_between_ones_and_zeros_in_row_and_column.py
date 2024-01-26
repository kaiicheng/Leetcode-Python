from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        row_one = []
        row_zero = []
        for i in range(len(grid)):
            cur_one = 0
            cur_zero = 0
            for j in range(len(grid[i])):
                # print("i, j: ", i, j)
                if grid[i][j] == 0:
                    cur_zero += 1
                elif grid[i][j] == 1:
                    cur_one += 1
            row_one.append(cur_one)
            row_zero.append(cur_zero)
        # print("row_one, row_zero: ", row_one, row_zero)

        col_one = []
        col_zero = []
        for i in range(len(grid[0])):
            cur_one = 0
            cur_zero = 0
            for j in range(len(grid)):
                # print("i, j: ", i, j)
                if grid[j][i] == 0:
                    cur_zero += 1
                elif grid[j][i] == 1:
                    cur_one += 1
            col_one.append(cur_one)
            col_zero.append(cur_zero)
        # print("col_one, col_zero: ", col_one, col_zero)

        ans = []
        for i in range(len(row_one)):
            cur = []
            for j in range(len(col_one)):
                cur.append(row_one[i] + col_one[j] - row_zero[i] - col_zero[j])
            ans.append(cur)
        return ans

def main(grid):
    result = Solution()
    print(result.onesMinusZeros(grid))

if __name__== "__main__" :
    grid = [[0,1,1],[1,0,1],[0,0,1]]
    main(grid)
