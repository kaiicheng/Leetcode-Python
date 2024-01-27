from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        c = Counter(arr)
        # print("c: ", c)
        ls = [[c[i], i] for i in c]
        ls.sort(reverse = True)
        # print("ls: ", ls)

        ans = 0
        n = len(arr)
        half = len(arr) // 2
        for i in range(len(ls)):
            # print("i: ", i)
            # print("n: ", n)
            if n - ls[i][0] <= half:
                ans += 1
                # print("break!")
                break
            else:
                n -= ls[i][0]
                ans += 1
            # print("---end of iteration---")
        return ans

def main(arr):
    result = Solution()
    print(result.minSetSize(arr))

if __name__== "__main__" :
    arr = [3,3,3,3,5,5,5,2,2,7]
    main(arr)
