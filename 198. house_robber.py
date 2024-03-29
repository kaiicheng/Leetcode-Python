from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        # maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        maxRobbedAmount = [None] * (len(nums) + 1)
        N = len(nums)
        
        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # print("i: ", i)

            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
            
            # print("maxRobbedAmount: ", maxRobbedAmount)

        return maxRobbedAmount[0]    

def main(nums):
    result = Solution()
    print(result.rob(nums))

if __name__== "__main__" :
    nums = [2,7,9,3,1]
    main(nums)
