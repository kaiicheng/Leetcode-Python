from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        ans = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j] and words[i] not in ans:
                        ans.append(words[i])
        return ans

def main(words):
    result = Solution()
    print(result.stringMatching(words))

if __name__== "__main__" :
    words = ["mass","as","hero","superhero"]
    main(words)