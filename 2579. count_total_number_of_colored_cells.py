# 1
# 1 + 4
# 1 + 4 + 8
# 1 + 4 + 8 + 12

class Solution:
    def coloredCells(self, n: int) -> int:
        
        if n == 1:
            return 1

        ans = 1
        for i in range(1, n):
            # print("i: ", i)
            ans += i * 4
            # print("ans: ", ans)

        return ans

def main(n):
    result = Solution()
    print(result.coloredCells(n))

if __name__== "__main__" :
    n = 3
    main(n)
