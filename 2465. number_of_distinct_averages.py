from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        s = set()
        nums.sort()
        # print("nums: ", nums)

        for i in range(len(nums) // 2):
            # print("l, r: ", i, len(nums) - i - 1)
            # print("n[l], n[r]: ", nums[i], nums[len(nums) - i - 1])
            # print("nums[l], nums[r]: ", nums[i], nums[len(nums) - i - 1])
            avg = (nums[i] +  nums[len(nums) - i - 1]) / 2
            s.add(avg)

        return len(s)

def main(nums):
    result = Solution()
    print(result.distinctAverages(nums))

if __name__== "__main__" :
    nums = [4,1,4,0,3,5]
    main(nums)
