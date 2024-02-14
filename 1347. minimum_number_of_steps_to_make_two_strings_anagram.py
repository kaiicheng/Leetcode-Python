class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        # initialize the count list for 26 letters
        count = [0] * 26

        # store the difference of frequencies of characters in t and s
        for i in range(len(s)):
            count[ord(t[i]) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] -= 1

        ans = 0
        # add the difference where string t has more instances than s
        for i in range(26):
            ans += max(0, count[i])

        return ans



        # wrong

        # c1 = Counter(s)
        # c2 = Counter(t)
        # print("c1: ", c1)
        # print("c2: ", c2)

        # if c1 == c2:
        #     return 0

        # # change the s to t
        # new_c1 = Counter()
        # ans = 0
        # for i in c1:
        #     print("i: ", i)
        #     # print("c1[i]: ", c1[i])
        #     if i not in c2:
        #         ans += c1[i]
        #         rest = c1[i]
        #         # while rest > 0:
        #         for j in c2:
        #             print("j: ", j)
        #             if j != i:
        #                 if j not in new_c1:
        #                     print("j (j != i, j not in new_c1): ", j)
        #                     print("c2[j], rest: ", c2[j], rest)
        #                     if c2[j] == rest:
        #                         new_c1[j] = c2[j]
        #                         rest = 0
        #                         print("break")
        #                         break
        #                     elif c2[j] > rest:
        #                         new_c1[j] = rest
        #                         rest = 0
        #                         break
        #                     elif c2[j] < rest:
        #                         new_c1[j] = c2[j]
        #                         rest -= c2[j]
        #             # if rest == 0:
        #             #     break
        #                 # elif j in new_c1:
        #         # new_c1[i] = 
        #         # delete c1[i]

        #     elif i in c2:
        #         if c1[i] != c2[i]:
        #             ans += abs(c1[i] - c2[i])
        #             new_c1[i] = c2[i]
        #             for j in c2:
        #                 print("j: ", j)
        #                 if j != i:
        #                     if j not in new_c1:
        #                         new_c1[j] = c2[j]
        #                         break
        #                     # elif j in new_c1:

        #         elif c1[i] == c2[i]:
        #             new_c1[i] = c2[i]           
        #     print("new_c1: ", new_c1)
        #     print("ans: ", ans)
        #     if new_c1 == c2:
        #         print("break!")
        #         break

        # # for i in c1:
        # #     for j in c2:
        # #         print("i, j: ", i, j)
        # #         # print("c1[i]: ", c1[i])
        # #         if i not in c2:

        # return ans
    
def main(s, t):
    result = Solution()
    print(result.minSteps(s, t))

if __name__== "__main__" :
    s = "leetcode"
    t = "practice"
    main(s, t)
