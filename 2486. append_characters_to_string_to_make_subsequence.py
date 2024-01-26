class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        count = 0
        j = 0
        for i in s:
            # print("i, j: ", i, j)
            if j == len(t):
                return 0
            if i == t[j]:
                j += 1
                count += 1
        return len(t) - count



        # wrong

        # mx = -1
        # mx_s = ""
        # l = 0
        # for r in range(1, len(t) + 1):
        #     print("l, r: ", l, r)
        #     cur = t[l:r]
        #     print("cur: ", cur)
        #     # f = s.find(cur)
        #     # print("f: ", f)
        #     if cur in s:
        #         mx = r - l
        #         mx_s = cur

        #     # if f >= 0:
        #     #     # print("found!")
        #     #     # print("i, s[:i]: ", i, s[:i])
        #     #     mx = r - l
        #     #     mx_s = cur
        #     # elif f == -1:
        #     #     l += 1
        #     print("---iteration---")
            
        # print("mx, mx_s: ", mx, mx_s)

        # if mx == -1:
        #     return len(t)
        # else:
        #     c = Counter(t)
        #     c_found = Counter(mx_s)
        #     print("c, c_found: ", c, c_found)
        #     for i in c_found:
        #         print("i: ", i)
        #         if i in c:
        #             c[i] -= c_found[i]
        #             if c[i] == 0:
        #                 del c[i]
        # # print("c, c_found: ", c, c_found)

        # return sum(c.values())

def main(s, t):
    result = Solution()
    print(result.appendCharacters(s, t))

if __name__== "__main__" :
    s = "coaching"
    t = "coding"
    main(s, t)
