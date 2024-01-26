from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:

        c = Counter(arr)
        # print("c: ", c)

        ls = []
        for i in range(len(arr)):
            # print("c[arr[i]], len(arr): ", c[arr[i]], len(arr))
            if c[arr[i]] == arr[i]:
                if arr[i] not in ls:
                    ls.append(arr[i])
        if len(ls) > 0:
            return max(ls)
        else:
            return -1

def main(arr):
    result = Solution()
    print(result.findLucky(arr))

if __name__== "__main__" :
    arr = [2,2,3,4]
    main(arr)


