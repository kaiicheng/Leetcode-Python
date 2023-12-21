from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            print("n: ", n)
            print("first, second: ", first_num, second_num)
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False



        # wrong

        # x = nums[0]
        # y = float("-inf")
        # z = float("-inf")

        # for i in range(1, len(nums)):

        #     if x < y and y < nums[i]:
        #         z = nums[i]
        #     elif x < nums[i]:
        #         y = nums[i]
            
        #     print("x, y, z: ", x, y, z)
        #     if x < y and y < z:
        #         return True
        # return False



        # wrong

        # mi = nums[0]
        # ans = [[0, nums[0]]]
        # for i in range(1, len(nums)):
        #     print("i, nums[i]: ", i, nums[i])
        #     print("ans, min: ", ans, mi)

        #     if i == 0:
        #         # ans.append([i, nums[i]])
        #         pass
        #     else:
        #         print("ans[-1][1]: ", ans[-1][1])
        #         if nums[i] < mi:
        #             mi = nums[i]
        #             ans = [[i, nums[i]]]
        #         else:
        #             if ans[-1][1] < nums[i]:
        #                 print("!3!")
        #                 ans.append([i, nums[i]])
        #             else:
        #                 # ans = []
        #                 # ans.append([i, nums[i]])
        #                 pass
        #     print("ans, min: ", ans, mi)
        #     if len(ans) >= 3:
        #         return True
        # return False



        # ans = [[0, nums[0]]]
        # for i in range(1, len(nums)):
        #     print("i, nums[i]: ", i, nums[i])
        #     print("ans: ", ans)

        #     if i == 0:
        #         # ans.append([i, nums[i]])
        #         pass
        #     else:
        #         print("ans[-1][1]: ", ans[-1][1])
        #         if ans[-1][1] < nums[i]:
        #             ans.append([i, nums[i]])
        #         else:
        #             ans = []
        #             ans.append([i, nums[i]])
        #     if len(ans) >= 3:
        #         return True
        # return False
    
def main(nums):
    result = Solution()
    print(result.increasingTriplet(nums))

if __name__== "__main__" :
    nums = [1,2,3,4,5]
    main(nums)
