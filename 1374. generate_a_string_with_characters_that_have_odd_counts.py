class Solution:
    def generateTheString(self, n: int) -> str:
        
        res = ""
        if n % 2 != 0:
            return "a" * n

        res = "a" * (n-1)
        return res + "b"

        # wrong

        # ls = []
        # i = 1
        # while n > 0:
        #     print("ls: ", ls)
        #     print("i: ", i)
        #     if n - i >= 0:
        #         ls.append(i)
        #     else:
        #         break
        #     # if n - i > 0 and n - i not in ls:
        #     #     ls.append(n - i)
        #     n -= i
        #     i += 2
        # print("ls: ", ls)

        # s = "abcdefghijklmnopqrstuvwxyz"

        # # for i in range(n):

def main(n):
    result = Solution()
    print(result.generateTheString(n))

if __name__== "__main__" :
    n = 7
    main(n)
