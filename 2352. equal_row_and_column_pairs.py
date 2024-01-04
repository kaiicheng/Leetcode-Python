from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        ans = 0
        # di = {}
        ls = []
        for i in range(len(grid)):
            # if grid[i] not in ls:
            #     ls.append(grid[i])

            for j in range(len(grid[i])):

                # print("i, j: ", i, j)
                temp = []
                for k in range(len(grid[i])):
                    # pass
                    temp.append(grid[k][j])
                    # print("temp: ", temp)
                    # print("grid[i]: ", grid[i])
                    if temp == grid[i]:
                        # print("---same!---")
                        ans += 1
            # print("---end---")

                # for k in range(len(grid)):
                #     temp = []
                #     for l in range(len(grid[k])):
                        
                #         temp.append(grid[l][k])
                #         print("temp: ", temp)
                #         print("grid[i]: ", grid[i])
                #         if 
                #             if temp == grid[i]:
                #                 print("---same!---")
                #                 ans += 1
        # print("ls: ", ls)
        return ans

def main(grid):
    result = Solution()
    print(result.equalPairs(grid))

if __name__== "__main__" :
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    main(grid)
