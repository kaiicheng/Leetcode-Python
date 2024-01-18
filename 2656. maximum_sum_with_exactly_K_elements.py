from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        x = max(nums)

        ans = 0
        for i in range(k):
            # print("ans: ", ans)
            # print("x: ", x)
            ans += x
            x += 1
        return ans

def main(nums, k):
    result = Solution()
    print(result.maximizeSum(nums, k))

if __name__== "__main__" :
    nums = [1,2,3,4,5]
    k = 3
    main(nums, k)
