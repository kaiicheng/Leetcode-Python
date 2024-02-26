from typing import List
from collections import defaultdict

class Solution:
    def countElements(self, arr: List[int]) -> int:

        di = defaultdict()
        for i in arr:
            di[i] = ""
        # print("di: ", di)

        ans = 0
        for i in range(len(arr)):
            if arr[i] + 1 in di:
                ans += 1
        
        return ans

def main(arr):
    result = Solution()
    print(result.countElements(arr))

if __name__== "__main__" :
    arr = [1,1,3,3,5,5,7,7]
    main(arr)
