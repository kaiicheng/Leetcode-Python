from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dynamic programming - bottom up
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
                print("dp: ", dp)

        # return dp[amount] if dp[amount] != float('inf') else -1 
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1



        # dynamic programming - top down
        # @lru_cache(None)
        # def dfs(rem):
        #     if rem < 0:
        #         return -1
        #     if rem == 0:
        #         return 0
        #     min_cost = float('inf')
        #     for coin in coins:
        #         res = dfs(rem - coin)
        #         if res != -1:
        #             min_cost = min(min_cost, res + 1)
        #     return min_cost if min_cost != float('inf') else -1

        # return dfs(amount)



        # wrong
        # coins.sort()
        
        # ans = 0
        # for i in reversed(range(len(coins))):
        #     print("i, coins[i]: ", i, coins[i])

        #     while amount - coins[i] >= 0:
        #         ans += 1
        #         amount -= coins[i]
        #     print("amount: ", amount)
        #     print("ans: ", ans)
        # print("ans: ", ans)

        # if amount > 0:
        #     return -1
        # else:
        #     return ans

def main(coins, amount):
    result = Solution()
    print(result.coinChange(coins, amount))

if __name__== "__main__" :
    coins = [1,2,5]
    amount = 11
    main(coins, amount)
