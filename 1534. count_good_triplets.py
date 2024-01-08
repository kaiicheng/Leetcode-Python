
import itertools
from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        # itertools.combinations
        cnt = 0
        for i, j, k in itertools.combinations(arr, 3):
            if abs(i-j) <= a and abs(j-k) <= b and abs(k-i) <= c:
                cnt +=1
        return cnt


        # ans = 0
        # for i in range(len(arr)):
        #     for j in range(i + 1, len(arr)):
        #         for k in range(j + 1, len(arr)):
        #             if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
        #                 ans += 1
        # return ans
    
def main(arr, a, b, c):
    result = Solution()
    print(result.countGoodTriplets(arr, a, b, c))

if __name__== "__main__" :
    arr = [3,0,1,1,9,7]
    a = 7
    b = 2
    c = 3
    main(arr, a, b, c)
