from typing import List

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        
        ans = -1
        mx = 0
        for i in range(len(grid)):
            temp = 0
            temp = sum(grid[i])
            mx = max(temp, mx)
            if mx == temp:
                ans = i
        return ans
    
def main(grid):
    result = Solution()
    print(result.findChampion(grid))

if __name__== "__main__" :
    grid = [[0,0,1],[1,0,1],[0,0,0]]
    main(grid)
