from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        ans = 0
        for i in range(len(patterns)):
            if patterns[i] in word:
                ans += 1
        return ans

def main(patterns, word):
    result = Solution()
    print(result.numOfStrings(patterns, word))

if __name__== "__main__" :
    patterns = ["a","abc","bc","d"]
    word = "abc"
    main(patterns, word)