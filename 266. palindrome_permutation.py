# Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.
# permutation!

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1
        # print(dict)
        # print(list(dict))

        dict = sorted(dict.items(), key=lambda x:x[1])
        print(dict)

        penalty = 1

        for i in range(len(dict)):
            print("dict[i]: ", dict[i])
            # print("dict[i][0]: ", dict[i][0])
            # print("dict[i][1]: ", dict[i][1])
            if dict[i][1] % 2 != 0:
                penalty -= 1
            if penalty < 0:
                return False
        return True

        # s_reversed = copy.deepcopy(s)
        # s_reversed = s_reversed[::-1]
        # print("s: ", s)
        # print("s_reversed: ", s_reversed)
        # for i in range(len(s)//2):
        #     if s[i] != s_reversed[i]:
        #         return False
        # return True

if __name__== "__main__" :
    # s = "code"
    # s = "carerac"
    s = "aab"
    result = Solution()
    print(result.canPermutePalindrome(s))