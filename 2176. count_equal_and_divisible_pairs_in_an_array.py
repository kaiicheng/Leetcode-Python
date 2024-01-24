from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    if nums[i] == nums[j] and (i * j) % k == 0:
                        # print("i, j: ", i, j)
                        ans += 1
        return ans

def main(nums, k):
    result = Solution()
    print(result.countPairs(nums, k))

if __name__== "__main__" :
    nums = [3,1,2,2,2,1,3]
    k = 2
    main(nums, k)
