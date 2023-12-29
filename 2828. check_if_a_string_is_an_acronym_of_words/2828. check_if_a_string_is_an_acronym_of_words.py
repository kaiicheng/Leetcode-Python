from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        ls = []
        for i in range(len(words)):
            ls.append(words[i][0])
        return s == "".join(ls)

def main(words, s):
    result = Solution()
    print(result.isAcronym(words, s))

if __name__== "__main__" :
    words = ["alice","bob","charlie"]
    s = "abc"
    main(words, s)
