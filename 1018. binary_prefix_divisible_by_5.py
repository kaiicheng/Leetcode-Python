# bin(10)  # '0b1010'
# int(0b1010, 2)  # 10

from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        # print(type(0b0))  # <class 'int'>
        # print(int(0b0))

        ans = []
        cur = 0
        for i in range(len(nums)):
            # print("i, nums[i]: ", i, nums[i])
            # print("cur * 2 + nums[i]: ", cur * 2 + nums[i])
            cur = cur * 2 + nums[i]
            # print("cur: ", cur)
            # print("int(cur, 2): ", int(cur, 2))

            if cur % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans



        # Time Limit Exceeded

        # ans = []
        # for i in range(1, len(nums) + 1):
        #     cur = nums[:i]
        #     cur = [str(i) for i in cur]
        #     cur = "".join(cur)

        #     # print("cur: ", cur)
        #     # print("int(cur, 2): ", int(cur, 2))

        #     if int(cur, 2) % 5 == 0:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        # return ans

def main(nums):
    result = Solution()
    print(result.prefixesDivBy5(nums))

if __name__== "__main__" :
    nums = [0,1,1]
    main(nums)
