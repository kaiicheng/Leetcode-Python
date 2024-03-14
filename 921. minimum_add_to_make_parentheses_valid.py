class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ans = 0
        bal = 0
        for i in s:
            if i == "(":
                bal += 1 
            else:
                bal -= 1
            print("bal: ", bal)
            # print("ans: ", ans)

            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1

        return ans + bal



        # wrong

        # s = list(s)
        # c = Counter(s)
        # print("c: ", c)

        # if c["("] == 0:
        #     return c[")"]
        # if c[")"] == 0:
        #     return c["("]
        
        # return max(c["("], c[")"]) - min(c["("], c[")"])

def main(s):
    result = Solution()
    print(result.minAddToMakeValid(s))

if __name__== "__main__" :
    s = "())"
    main(s)
