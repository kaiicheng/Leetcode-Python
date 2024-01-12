# find the longest string of a list
# print(max(["1", "12", "123"], key=len))  # "123"

# iterate the column of matrix

# matrix = [[1, 2, 3], [4, 5, 6]]
# for col in range(len(matrix[0])):
#     column = [row[col] for row in matrix]
#     print(f"Column {col}: {column}")

# matrix = [[1, 2, 3], [4, 5, 6]]
# for col in range(len(matrix[0])):
#     column = []
#     for row in matrix:
#         column.append(row[col])
#     print(f"Column {col}: {column}")

from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        ans = []
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                # print("i, j, grid[i][j]: ", i, j, grid[i][j])
                # print("j, i, grid[j][i]: ", j, i, grid[j][i])
                col.append(str(grid[j][i]))
            mx = max(col, key=len)
            ans.append(len(mx))
            # print("col: ", col)
        # print("ans: ", ans)
        return ans



        # wrong

        # ans = []
        # for i in range(len(grid)):
        #     col = []
        #     # print("len(grid[i]): ", len(grid[i]))
        #     if len(grid[i]) == 1:
        #         col = [str(i[0]) for i in grid]
        #         print("col: ", col)
        #         mx = max(col, key=len)
        #         ans.append(len(mx))
        #         break
        #     else:
        #         for j in range(len(grid[i])):
        #             print("i, j, grid[i][j]: ", i, j, grid[i][j])
        #             # print("j, i, grid[j][i]: ", j, i, grid[j][i])
        #             col.append(str(grid[j][i]))
        #     mx = max(col, key=len)
        #     ans.append(len(mx))
        #     print("col: ", col)
        # print("ans: ", ans)
        # return ans

def main(grid):
    result = Solution()
    print(result.findColumnWidth(grid))

if __name__== "__main__" :
    grid = [[-15,1,3],[15,7,12],[5,6,-2]]
    main(grid)
