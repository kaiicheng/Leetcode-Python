from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        ans = 0
        l = 0
        while l < len(words):
            for r in range(len(words)):
                if l != r:
                # for j in range(i + 1, len(words)):
                    if set(words[l]) == set(words[r]):
                        # print("l, r: ", l, r)
                        ans += 1
            l += 1
        return ans // 2

def main(words):
    result = Solution()
    print(result.similarPairs(words))

if __name__== "__main__" :
    words = ["aba","aabb","abcd","bac","aabc"]
    main(words)