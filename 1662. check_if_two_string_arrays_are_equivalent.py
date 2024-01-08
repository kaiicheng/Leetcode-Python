from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
    
def main(word1, word2):
    result = Solution()
    print(result.arrayStringsAreEqual(word1, word2))

if __name__== "__main__" :
    word1  = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    main(word1, word2)