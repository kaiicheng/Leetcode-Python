from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        ls = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                # if i != j:
                # print("i, j: ", i, j)
                if abs(i - j) <= k and nums[j] == key:
                    ls.append(i)
                    break
            # print("ls: ", ls)
        # ls = set(ls)
        # ls = list(ls)
        ls.sort()
        return ls

def main(nums, key, k):
    result = Solution()
    print(result.findKDistantIndices(nums, key, k))

if __name__== "__main__" :
    nums = [3,4,9,1,3,9,5]
    key = 9
    k = 1
    main(nums, key, k)
