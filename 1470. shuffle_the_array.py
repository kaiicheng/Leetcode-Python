from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        ls = []
        for i in range(n):
            temp = []
            for j in range(len(nums)):
                if j % n == i:
                    temp.append(nums[j])
            ls.append(temp)
        # print("ls: ", ls)

        ans = []
        for i in range(len(ls)):
            ans = ans + ls[i]

        return ans

def main(nums, n):
    result = Solution()
    print(result.shuffle(nums, n))

if __name__== "__main__" :
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    main(nums, n)

