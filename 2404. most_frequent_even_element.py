from typing import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        ls = []
        for i in c:
            ls.append([c[i], i])
        ls.sort(reverse=True)
        # print("ls: ", ls)

        ans = None
        freq = None
        for i in range(len(ls)):
            if freq is not None and ans is not None and freq > ls[i][0]:
                break
            else:
                if ls[i][1] % 2 == 0:
                    ans = ls[i][1]
                    freq = ls[i][0]
        if ans == None:
            return -1
        else:
            return ans

def main(nums):
    result = Solution()
    print(result.mostFrequentEven(nums))

if __name__== "__main__" :
    nums = [0,1,2,2,4,4,1]
    main(nums)
