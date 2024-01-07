from typing import List

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        
        v = "aeiou"

        ans = 0
        for i in range(len(words)):
            if left <= i and i <= right:
                # print("i, words[i]: ", i, words[i])
                if words[i][0] in v and words[i][-1] in v:
                    ans += 1
        return ans

def main(words, left, right):
    result = Solution()
    print(result.vowelStrings(words, left, right))

if __name__== "__main__" :
    words = ["hey","aeo","mu","ooo","artro"]
    left = 1
    right = 4
    main(words, left, right)
