# interesting! 
# ls = [[]] * len(di)
# ls[0].append(1)
# ls[0].append(2)
# print("ls: ", ls)

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        # c = Counter(order)
        # print("c: ", c)
        
        di = {}
        for i in range(len(order)):
            di[order[i]] = i
        # print("di: ", di)

        # interesting! 
        # ls = [[]] * len(di)
        # ls[0].append(1)
        # ls[0].append(2)
        # print("ls: ", ls)

        ls = [[] for i in range(len(order))]
        # print("ls: ", ls)

        res = []
        for i in range(len(s)):
            # print("i, s[i]: ", i, s[i])
            if s[i] in di:
                # print("di[s[i]]: ", di[s[i]])
                ls[di[s[i]]].append(s[i])
            else:
                res.append(s[i])
            # print("ls: ", ls)
        # print("ls: ", ls)
        # print("res: ", res)

        ans = ls[0]
        for i in range(1, len(ls)):
            ans = ans + ls[i]
        # print("ans: ", ans)
        ans = ans + res

        return "".join(ans)

def main(order, s):
    result = Solution()
    print(result.customSortString(order, s))

if __name__== "__main__" :
    order = "cbafg"
    s = "abcd"
    main(order, s)
