from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        c = Counter(s)
        # print("c: ", c)
        ls = []
        for i in c:
            ls.append(c[i])
        
        s = set(ls)
        # print("s: ", s)

        if len(s) == 1:
            return True
        else:
            return False

def main(s):
    result = Solution()
    print(result.areOccurrencesEqual(s))

if __name__== "__main__" :
    s = "aaabb"
    main(s)
