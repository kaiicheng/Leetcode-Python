from typing import List

# .insert()
# vowel = ['a', 'e', 'i', 'u']
# vowel.insert(3, 'o')
# print('List:', vowel)

# .remove(element)

# del list[]

# .pop(index)

# Output: List: ['a', 'e', 'i', 'o', 'u']
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        
        # greedy

        # mx = 0
        # cur = 0
        # for i in range(len(nums) - 1, -1, -1):
        #     # print("i, nums[i], mx, cur: ", i, nums[i], mx, cur)
        #     if cur < nums[i]:
        #         cur = nums[i]
        #     else:
        #         cur += nums[i]
        #     mx = max(mx, cur)
        # return mx



        # in-place, iterate backwards

        for i in range(len(nums) - 1, 0, -1):
            print("i: ", i)
            if nums[i - 1] <= nums[i]:
                nums[i - 1] = nums[i - 1] + nums[i]
            print("nums: ", nums)
        return nums[0]



        # wrong

        # i = 0
        # mx = float("-inf")
        # for _ in range(len(nums) - 1 - 1):
        #     if nums[i] <= nums[i + 1]:
        #         print("i: ", i)
        #         temp = nums[i] + nums[i + 1]
        #         mx = max(mx, temp)
        #         nums.pop(i)
        #         nums.pop(i)
        #         nums.insert(0, temp)
        #     else:
        #         i += 1
        #     print("nums: ", nums)
        # print("mx: ", mx)
        # return mx

def main(nums):
    result = Solution()
    print(result.maxArrayValue(nums))

if __name__== "__main__" :
    nums = [2,3,7,9,3]
    main(nums)
