from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        xy = 0
        xz = 0
        yz = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print("i, j: ", i, j)
                if grid[i][j] != 0:
                    xy += 1
        # print("xy, xz, yz: ", xy, xz, yz)

        for i in range(len(grid)):
            # print("i: ", i)
            xz += max(grid[i])
            # for j in range(len(grid[i])):
            #     print("i, j: ", i, j)
            #     if grid[i][j] != 0:
            #         xy += 1
        # print("xy, xz, yz: ", xy, xz, yz)

        mx = float("-inf")
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print("i, j: ", i, j)
                # print("grid[j][i]: ", grid[j][i])
                mx = max(mx, grid[j][i])
                # if temp1
                # yz += max(grid[j])
            # print("mx: ", mx)
            yz += mx
            mx = float("-inf")

            #     if i == len(grid) - 1:
            #         yz += grid[i][j]
        # print("xy, xz, yz: ", xy, xz, yz)

        return xy + xz + yz

def main(grid):
    result = Solution()
    print(result.projectionArea(grid))

if __name__== "__main__" :
    grid = [[1,2],[3,4]]
    main(grid)
