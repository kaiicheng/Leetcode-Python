from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        wealth = []
        for i in range(len(accounts)):
            wealth.append(sum(accounts[i]))
        return max(wealth)

def main(accounts):
    result = Solution()
    print(result.maximumWealth(accounts))

if __name__== "__main__" :
    accounts = [[1,2,3],[3,2,1]]
    main(accounts)
