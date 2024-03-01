from collections import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        pre = []
        for i in range(len(words)):
            pre.append(words[i])
            temp_pre = "".join(pre)
            if s.find(temp_pre) == 0:
                if temp_pre == s:
                    return True
            else:
                return False

def main(s, words):
    result = Solution()
    print(result.isPrefixString(s, words))

if __name__== "__main__" :
    s = "iloveleetcode"
    words = ["i","love","leetcode","apples"]
    main(s, words)
