from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        ls = [i + 1 for i in range(k)]
        # print("ls: ", ls)
        for i in range(len(nums) - 1, -1, -1):
            # print("i: ", i)
            if nums[i] in ls:
                ls.remove(nums[i])
            # print("ls: ", ls)
            if len(ls) == 0:
                return len(nums) - i

def main(nums, k):
    result = Solution()
    print(result.minOperations(nums, k))

if __name__== "__main__" :
    nums = [3,1,5,4,2]
    k = 2
    main(nums, k)
