from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        c = Counter(arr)
        ls = []
        for i in c:
            if c[i] not in ls:
                ls.append(c[i])
            else:
                return False
        return True

def main(arr):
    result = Solution()
    print(result.uniqueOccurrences(arr))

if __name__== "__main__" :
    arr = [1,2,2,1,1,3]
    main(arr)
