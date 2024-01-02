from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        # math

        # ans = [0] * len(pref)
        # ans[0] = pref[0]
        # for i in range(1, len(pref)):
        #     ans[i] = pref[i] ^ pref[i - 1]
        # return ans



        # math space optimized
        
        for i in reversed(range(len(pref))):
            pref[i] = pref[i] ^ pref[i - 1]
        return pref


def main(pref):
    result = Solution()
    print(result.findArray(pref))

if __name__== "__main__" :
    pref = [5,2,0,3,1]  # [5,7,2,3,2]
    main(pref)

