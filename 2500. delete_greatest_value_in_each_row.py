from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        # if len()

        ans = []
        temp = []
        while len(grid[0]) >= 1:
            for i in range(len(grid)):
                # print("i: ", i)
                # temp = []
                # print("grid[i]: ", grid[i])
                temp.append(max(grid[i]))
                grid[i].remove(max(grid[i]))
                
            # print("grid: ", grid)
            # print("temp: ", temp)
            ans.append(max(temp))
            temp = []
            # print("ans: ", ans)
        return sum(ans)



        # wrong

        # ans = []
        # for i in range(len(grid[0])):
        #     temp = []
        #     for j in range(len(grid)):
        #         print("i, j: ", i, j)
        #         print("grid[j][i]: ", grid[j][i])
        #         temp.append(grid[j][i])

        #     print("temp: ", temp)
        #     ans.append(max(temp))
        # print("ans: ", ans)
        # return sum(ans)

def main(grid):
    result = Solution()
    print(result.deleteGreatestValue(grid))

if __name__== "__main__" :
    grid = [[1,2,4],[3,3,1]]
    main(grid)
