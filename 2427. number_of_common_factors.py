class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        n = min(a, b)
        ans = 0
        for i in range(1, n + 1):
            # print("i: ", i)
            # if a // i == int(a / i) and b // i == int(b / i):
            if a % i == 0 and b % i == 0:
                # print("ans += 1!")
                ans += 1
        return ans

def main(a, b):
    result = Solution()
    print(result.commonFactors(a, b))

if __name__== "__main__" :
    a = 25
    b = 30
    main(a, b)
