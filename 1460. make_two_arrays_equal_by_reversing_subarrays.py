from collections import Counter
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # print("Counter(target), Counter(arr): ", Counter(target), Counter(arr))
        return Counter(target) == Counter(arr)

def main(target, arr):
    result = Solution()
    print(result.canBeEqual(target, arr))

if __name__== "__main__" :
    target = [1,2,3,4]
    arr = [2,4,1,3]
    main(target, arr)
