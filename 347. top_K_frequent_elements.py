# heap

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # # O(1) time 
        # if k == len(nums):
        #     return nums
        
        # # 1. Build hash map: character and how often it appears
        # # O(N) time
        # count = Counter(nums)   
        # # 2-3. Build heap of top k frequent elements and
        # # convert it into an output array
        # # O(N log k) time
        # return heapq.nlargest(k, count.keys(), key=count.get) 

        c = Counter(nums)
        # print("c: ", c)

        ls = list(c.items())
        # print("ls: ", ls)

        ls = sorted(ls, key=lambda ls: ls[1], reverse=True)
        # print("ls: ", ls)

        ans = []
        for i in range(k):
            # print("i, ls[i]: ", i, ls[i])
            ans.append(ls[i][0])

        return ans
    
def main(nums, k):
    result = Solution()
    print(result.topKFrequent(nums, k))

if __name__== "__main__" :
    nums = [1,1,1,2,2,3]
    k = 2
    main(nums, k)
