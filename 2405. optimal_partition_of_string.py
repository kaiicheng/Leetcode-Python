class Solution:
    def partitionString(self, s: str) -> int:

        # hashmap

        # curset=set()
        # res=1
        # for c in s:
        #     # print("c: ", c)
        #     # print("curset: ", curset)
        #     if c in curset:
        #         res+=1
        #         curset=set()
        #     curset.add(c)
        #     # print("curset: ", curset)
        #     # print("res: ", res)
        #     # print("---end of iteration---")
        # return res



        # greedy

        # lastSeen = [-1] * 26
        # count = 1
        # substringStarting = 0

        # for i in range(len(s)):
        #     print("i, s[i]: ", i, s[i])
        #     print("substringStarting: ", substringStarting)
        #     print("lastSeen: ", lastSeen)
        #     if lastSeen[ord(s[i]) - ord('a')] >= substringStarting:
        #         count += 1
        #         substringStarting = i
        #     lastSeen[ord(s[i]) - ord('a')] = i

        # return count



        ls = []
        temp = ""
        di = {}
        ans = 1
        for i in range(len(s)):
            # print("i, s[i]: ", i, s[i])
            # print("di: ", di)

            if s[i] in di:
                di = {}
                ls.append(temp)
                temp = ""
                ans += 1

            temp = temp + s[i]
            di[s[i]] = ""

            ls.append
            # print("di: ", di)
            # print("temp: ", temp)
            # print("---end of iteration---")
        
        if len(temp) >= 1:
            ls.append(temp)

        # print("ls: ", ls)

        return len(ls)

def main(s):
    result = Solution()
    print(result.partitionString(s))

if __name__== "__main__" :
    s = "abacaba"
    main(s)
