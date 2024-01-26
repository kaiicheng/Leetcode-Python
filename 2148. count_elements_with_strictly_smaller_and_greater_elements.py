from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        ans = 0
        for i in range(len(nums)):
            low = nums[i]
            high = nums[i]
            inc = False
            dec = False
            for j in range(len(nums)):
                if i != j:
                    # print("i, j: ", i, j)
                    if high > nums[j]:
                        dec = True
                    if low < nums[j]:
                        inc = True
                    if dec and inc:
                        ans += 1
                        break
        return ans

def main(nums):
    result = Solution()
    print(result.countElements(nums))

if __name__== "__main__" :
    nums = [11,7,2,15]
    main(nums)
