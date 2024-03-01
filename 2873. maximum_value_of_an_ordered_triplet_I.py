from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        mx = float("-inf")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] - nums[j]) * nums[k] > mx:
                        # print("i, j, k: ", i, j, k)
                        # print("nums[i], nums[j], nums[k]: ", nums[i], nums[j], nums[k])
                        mx = max(mx, (nums[i] - nums[j]) * nums[k])
                        # print("mx: ", mx)
        if mx < 0:
            return 0
        else:
            return mx

def main(nums):
    result = Solution()
    print(result.maximumTripletValue(nums))

if __name__== "__main__" :
    nums = [12,6,1,2,7]
    main(nums)
