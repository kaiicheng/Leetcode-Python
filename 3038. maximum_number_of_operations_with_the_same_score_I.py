from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        score = nums[0] + nums[1]
        ans = 1
        for i in range(2, len(nums), 2):
            # print("i: ", i)
            if i == len(nums) - 1:
                break
            else:
                temp = nums[i] + nums[i + 1]
                if temp == score:
                    ans += 1
                else:
                    break
        return ans

def main(nums):
    result = Solution()
    print(result.maxOperations(nums))

if __name__== "__main__" :
    nums = [3,2,1,4,5]
    main(nums)
