# for loop continue

# count=0
# for string in 'content':
#     count+=1
#     if string == 't':
#         continue
#     print(string)

# c
# o
# n
# e
# n

import copy
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        a = copy.deepcopy(arr)
        a.sort()
        # print("a: ", a)
        mi = float("inf")
        for i in range(len(a) - 1):
            temp = abs(a[i + 1] - a[i])
            mi = min(mi, temp)
        # print("mi: ", mi)

        ans = []
        for i in range(len(a)):
            for j in range(i, len(a)):
                if i >= j:
                    continue
                else:
                    if abs(a[i] - a[j]) > mi:
                        break
                    else:
                        temp = abs(a[i + 1] - a[i])
                        if temp == mi:
                            ans.append([a[i], a[j]])
        # print("ans: ", ans)

        return ans
    
def main(arr):
    result = Solution()
    print(result.minimumAbsDifference(arr))

if __name__== "__main__" :
    arr = [4,2,1,3]
    main(arr)
