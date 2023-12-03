from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # sliding window

        if len(nums) == 1:
            return nums[0] / k
        
        # if len(nums) == k:
        #     return sum(nums) / k

        temp = sum(nums[0:0 + k])
        print("temp: ", temp)
        ans = temp

        for i in range(1, len(nums) - k + 1):
            # print("i: ", i)

            # print("nums[i:i + k]: ", nums[i:i + k])
            temp = temp - nums[i - 1] + nums[i + k - 1]

            # for j in range(k):
            #     # print("j: ", j)
            #     temp += nums[i + j]

            print("temp: ", temp)
            ans = max(ans, temp)
            # print("ans: ", ans)
        return ans/k



        # Time Limit Exceeded

        # while len(nums) == 1:
        #     return nums[0] / k

        # ans = float("-inf")
        # for i in range(len(nums) - k + 1):
        #     # print("i: ", i)

        #     # print("nums[i:i + k]: ", nums[i:i + k])
        #     temp = sum(nums[i:i + k])

        #     # for j in range(k):
        #     #     # print("j: ", j)
        #     #     temp += nums[i + j]

        #     # print("temp: ", temp)
        #     ans = max(ans, temp)
        #     # print("ans: ", ans)
        # return ans/k



        # Time Limit Exceeded

        # while len(nums) == 1:
        #     return nums[0] / k

        # ans = float("-inf")
        # for i in range(len(nums) - k + 1):
        #     # print("i: ", i)
        #     temp = 0
        #     for j in range(k):
        #         # print("j: ", j)
        #         temp += nums[i + j]
        #     # print("temp: ", temp)
        #     ans = max(ans, temp)
        #     # print("ans: ", ans)
        # return ans/k

def main(nums, k):
    result = Solution()
    print(result.findMaxAverage(nums, k))

if __name__== "__main__" :
    # nums = [1,12,-5,-6,50,3]
    # k = 4
    # nums = [0,1,1,3,3]
    # k = 4
    nums = [9,7,3,5,6,2,0,8,1,9]
    k = 6
    main(nums, k)
