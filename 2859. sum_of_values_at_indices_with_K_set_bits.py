from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        
        ans = []
        for i in range(len(nums)):
            # print("nums[i], bin(nums[i][2:]): ", nums[i], bin(nums[i])[2:])
            # print("str(bin(nums[i])[2:]).count('1'): ", str(bin(nums[i])[2:]).count("1"))
            if k == str(bin(i)[2:]).count("1"):
                ans.append(nums[i])
        # print("ans: ", ans)
        return sum(ans)

def main(nums, k):
    result = Solution()
    print(result.sumIndicesWithKSetBits(nums, k))

if __name__== "__main__" :
    nums = [5,10,1,5,2]
    k = 1
    main(nums, k)
