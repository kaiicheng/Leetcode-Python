from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                return words[i]
        return ""

def main(words):
    result = Solution()
    print(result.firstPalindrome(words))

if __name__== "__main__" :
    words = ["abc","car","ada","racecar","cool"]
    main(words)