class Solution:
    def climbStairs(self, n: int) -> int:

        # dynamic programming
        if n == 1:
            return 1
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        print("dp: ", dp)
        return dp[n - 1]



        # fibonacci number

        # if n == 1:
        #     return 1

        # first = 1
        # second = 2
        # for i in range(3, n + 1):
        #     print("i: ", i)
        #     third = first + second
        #     print("first, second, third: ", first, second, third)
        #     first = second
        #     second = third
        # return second



        # recursion with memoization

        # def count(i, n):
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
        #     if memo[i] > 0:
        #         return memo[i]
        #     memo[i] = count(i + 1, n) + count(i + 2, n)
        #     print("memo: ", memo)
        #     return memo[i]
        
        # memo = [0] * n
        # return count(0, n)




        # Time Limit Exceeded
        # brute force 

        # def count(i, n):
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
        #     return count(i + 1, n) + count(i + 2, n)
        
        # return count(0, n)

def main(n):
    result = Solution()
    print(result.climbStairs(n))

if __name__== "__main__" :
    n = 5
    main(n)
