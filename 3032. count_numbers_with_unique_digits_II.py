from collections import Counter

class Solution:
    def numberCount(self, a: int, b: int) -> int:
        
        ans = 0
        for i in range(a, b + 1):
            ls = list(str(i))
            c = Counter(ls)
            if len(ls) == len(c):
                ans += 1
        return ans

def main(nums):
    result = Solution()
    print(result.numberCount(nums))

if __name__== "__main__" :
    nums = [1,2,3,4]
    main(nums)
