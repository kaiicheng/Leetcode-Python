from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        ls = []
        for i in range(len(nums)):
            # print("i: ", i)
            for j in range(nums[i][0], nums[i][1] + 1):
                # print("j: ", j)
                if j not in ls:
                    ls.append(j)
        return len(ls)

def main(nums):
    result = Solution()
    print(result.numberOfPoints(nums))

if __name__== "__main__" :
    nums = [[3,6],[1,5],[4,7]]
    main(nums)
