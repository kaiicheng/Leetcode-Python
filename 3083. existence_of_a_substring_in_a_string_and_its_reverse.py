import copy

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        
        reverse = copy.deepcopy(s)
        reverse = reverse[::-1]
        # print("reverse: ", reverse)
        
        for i in range(len(s) - 1):
            # print("s[i: i + 1 + 1]: ", s[i: i + 1 + 1])
            if s[i: i + 1 + 1] in reverse:
                return True
        
        return False

def main(s):
    result = Solution()
    print(result.isSubstringPresent(s))

if __name__== "__main__" :
    s = "leetcode"
    main(s)
