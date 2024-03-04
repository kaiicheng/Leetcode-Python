from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        ans = []
        for i in range(len(prices)):
            found = False
            for j in range(i + 1, len(prices)):
                # print("i, j: ", i, j)
                if prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    found = True
                    break
            if not found:
                ans.append(prices[i])
        return ans

def main(prices):
    result = Solution()
    print(result.finalPrices(prices))

if __name__== "__main__" :
    prices = [8,4,6,2,3]
    main(prices)
