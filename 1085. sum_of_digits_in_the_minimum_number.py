from typing import List

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        
        n = min(nums)
        n = str(n)
        ans = 0
        for i in range(len(n)):
            ans += int(n[i])
        if ans % 2 == 0:
            return 1
        else:
            return 0

def main(nums):
    result = Solution()
    print(result.sumOfDigits(nums))

if __name__== "__main__" :
    nums = [34,23,1,24,75,33,54,8]
    main(nums)