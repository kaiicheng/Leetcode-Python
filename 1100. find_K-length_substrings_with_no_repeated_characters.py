from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
    
        ans = []
        for i in range(len(s) - k + 1):
            # print("i: ", i)
            cur = s[i:i+k]
            # print("cur: ", cur)
            if len(Counter(cur)) == k:
                ans.append(cur)
        # print("ans: ", ans)
        return len(ans)



        # wrong

        # print("len(s), s[len(s)]: ", len(s), s[len(s) - 1])

        # if len(s) < k:
        #     return 0

        # ls = []
        # l = 0
        # cur = [s[0]]
        # while l < len(s) - 1:
        #     print("l: ", l)
        #     for r in range(l, len(s)):
        #         print("---start of for loop---")
        #         print("l, r, cur: ", l, r, cur)
        #         print("s[r]: ", s[r])
        #         if s[r] not in cur:
        #             cur.append(s[r])
        #         else:
        #             # l = r
        #             print("l, s[l]: ", l, s[l])
        #             cur = [s[l]]
        #             break
        #         print("cur: ", cur)
        #         if len(cur) == k:
        #             # if "".join(cur) not in ls:
        #             ls.append("".join(cur))
        #             cur = []
        #             break

        #     l += 1
        #     # cur = [s[l]]
        # print("ls: ", ls)
        # return len(ls)

def main(s, k):
    result = Solution()
    print(result.numKLenSubstrNoRepeats(s, k))

if __name__== "__main__" :
    s = "havefunonleetcode"
    k = 5
    main(s, k)
