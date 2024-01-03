from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        ls1 = s1.split(" ")
        ls2 = s2.split(" ")

        # print("ls1, ls2: ", ls1, ls2)
        ls = ls1 + ls2
        c = Counter(ls)
        # print("ls: ", c) 

        ans = []
        for i in c:
            # print("i: ", i)
            if c[i] == 1:
                ans.append(i)

        return ans



        # wrong

        # ls1 = s1.split(" ")
        # ls2 = s2.split(" ")

        # ans = []
        # for i in range(len(ls1)):
        #     if ls1[i] not in ls2 and ls1[i] not in ans:
        #         ans.append(ls1[i])
        
        # for j in range(len(ls2)):
        #     if ls2[j] not in ls1 and ls2[j] not in ans:
        #         ans.append(ls2[j])
        
        # return ans
        
def main(s1, s2):
    result = Solution()
    print(result.uncommonFromSentences(s1, s2))

if __name__== "__main__" :
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    main(s1, s2)
