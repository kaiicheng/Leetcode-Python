class Solution:
    def bitwiseComplement(self, n: int) -> int:

        # print("n: ", n)
        # print("bin(n): ", bin(n))

        digit = bin(n)[2:]
        print("digit: ", digit)

        ans = []
        for i in range(len(digit)):
            if digit[i] == "0":
                ans.append("1")
            else:
                ans.append("0")
        print("ans: ", ans)
        ans = "".join(ans)
        print("int(ans): ", int(ans, 2))
        return int(ans, 2)
        
def main(n):
    result = Solution()
    print(result.bitwiseComplement(n))

if __name__== "__main__" :
    n = 10
    main(n)
