from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        s = set(allowed)
        ans = 0
        for i in range(len(words)):
            temp = set(words[i])
            valid = False
            for j in temp:
                if j in s:
                    valid = True
                    pass
                else:
                    valid = False
                    break
            if valid:
                ans += 1
        return ans
    
def main(allowed, words):
    result = Solution()
    print(result.countConsistentStrings(allowed, words))

if __name__== "__main__" :
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    main(allowed, words)
