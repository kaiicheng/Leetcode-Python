# Python XOR operation
# print(5^3)  # 6
# print(3^5)  # 6

# 5 = 0101(b)
# 3 = 0011(b)
# 0^0 ->0
# 1^0 ->1
# 0^1 ->1
# 1^1 ->0
# => 0110(b)：6

from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        ls = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    if [nums[i], nums[j]] not in ls and [nums[j], nums[i]] not in ls:
                        ls.append([nums[i], nums[j]])
        # print("ls: ", ls)

        mx = 0
        for i in range(len(ls)):
            mx = max(mx, ls[i][0] ^ ls[i][1])

        return mx

def main(nums):
    result = Solution()
    print(result.maximumStrongPairXor(nums))

if __name__== "__main__" :
    nums = [1,2,3,4,5]
    main(nums)
