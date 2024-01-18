from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors.sort()
        ls = []
        for i in range(len(divisors)):
            temp = 0
            for j in range(len(nums)):
                if nums[j] >= divisors[i] and nums[j] % divisors[i] == 0:
                    temp += 1
            ls.append(temp)
        # print("ls: ", ls)
        return divisors[ls.index(max(ls))]

def main(nums, divisors):
    result = Solution()
    print(result.maxDivScore(nums, divisors))

if __name__== "__main__" :
    nums = [4,7,9,3,9]
    divisors = [5,2,3]
    main(nums, divisors)
