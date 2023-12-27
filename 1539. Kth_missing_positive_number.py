from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        end = arr[-1]
        ls = []
        for i in range(1, end):
            if i not in arr:
                ls.append(i)
        # print("ls: ", ls)

        if k <= len(ls):
            return ls[k - 1]
        else:
            k -= len(ls)
            return end + k

def main(arr, k):
    result = Solution()
    print(result.findKthPositive(arr, k))

if __name__== "__main__" :
    arr = [1,2,3,4]
    k = 2
    main(arr, k)
