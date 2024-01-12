from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        ans = 0
        for i in range(len(words)):
            if words[i].find(pref) == 0:
                ans += 1
        return ans
    
def main(words):
    result = Solution()
    print(result.prefixCount(words))

if __name__== "__main__" :
    words = ["pay","attention","practice","attend"]
    pref = "at"
    main(c)
