from collections import Counter
from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        c = []
        for i in range(len(A)):
            temp1 = A[:i + 1]
            temp2 = B[:i + 1]
            c1 = Counter(temp1)
            c2 = Counter(temp2)
            common = 0
            for i in c1:
                # print("i, j: ", i)
                if i in c2:
                    common += 1
            # print("temp: ", temp)
            # s = Counter(temp)
            c.append(common)
        return c

def main(A, B):
    result = Solution()
    print(result.findThePrefixCommonArray(A, B))

if __name__== "__main__" :
    A = [1,3,2,4]
    B = [3,1,2,4]
    main(A, B)
