class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        di = {"0":"0", "1": "1", "2": "5", "5": "2", "6": "9", "8": "8", "9": "6"}
        # print("di: ", di)

        # ls = []
        ans = 0
        for i in range(1, n + 1):
            # print("i: ", i)
            s = str(i)
            temp = []
            # all_in_di = None
            for j in range(len(s)):
                # print("j: ", j)
                if s[j] in di:
                    # all_in_di = True
                    temp.append(di[s[j]])
                else:
                    # all_in_di = False
                    temp.append(s[j])

            if "3" not in temp and "4" not in temp and "7" not in temp:
                # print("s: ", s)
                # print("''.join(temp): ", "".join(temp))
                if s != "".join(temp):
                    # print("ans+1!")
                    ans += 1
            # print("---end of iteration---")

        return ans

def main(n):
    result = Solution()
    print(result.rotatedDigits(n))

if __name__== "__main__" :
    n = 857
    main(n)
