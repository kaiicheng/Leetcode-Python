from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        # ans = 0
        # nums.sort(reverse=True)
        # print("nums: ", nums)

        pos = []
        neg = []
        zero = []
        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            elif nums[i] > 0:
                pos.append(nums[i])
            elif nums[i] == 0:
                zero.append(nums[i])

        if len(pos) == 0:
            return 0
        else:
            pos.sort()
            # print("pos: ", pos)
            neg.sort(reverse=True)
            # print("neg: ", neg)
            # print("zero: ", zero)

            ans = len(pos)
            total = sum(pos)
            ls = pos
            for i in range(len(neg)):
                # print("i, neg[i]: ", i, neg[i])
                # print("total: ", total)
                if total + neg[i] > 0:
                    ls.append(neg[i])
                    ans += 1
                    total += neg[i]
                elif total + neg[i] <= 0:
                    break
                # print("ls: ", ls)
                # print("ans: ", ans)
            ans += len(zero)
            ls = ls + zero
            # print("ls: ", ls)
            return ans

def main(nums):
    result = Solution()
    print(result.maxScore(nums))

if __name__== "__main__" :
    nums = [2,-1,0,1,-3,3,-3]
    main(nums)
