from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # bit manipulation
        # If we take XOR of zero and some bit, it will return that bit
        # a⊕0=a
        # If we take XOR of two same bits, it will return 0
        # a⊕a=0
        # a⊕b⊕a=(a⊕a)⊕b=0⊕b
        ans = 0
        for i in nums:
            ans ^= i
        return ans


        # hash table

        # c = Counter(nums)
        # # print("c: ", c)
        # ans = [i for i in c if c[i] == 1]
        # # print("ans: ", ans)
        # return ans[0]



        # math
        # 2∗(a+b+c)−(a+a+b+b+c)=c

        # return 2 * sum(set(nums)) - sum(nums)

def main(nums):
    result = Solution()
    print(result.singleNumber(nums))

if __name__== "__main__" :
    nums = [4,1,2,1,2]
    main(nums)
