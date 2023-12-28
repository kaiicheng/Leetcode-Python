class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        price = 0
        if purchaseAmount < 10:
            if purchaseAmount < 5:
                price = 0
            else:
                price = 10
        elif purchaseAmount % 10 == 0:
            price = purchaseAmount
        elif purchaseAmount % 10 != 0:
            if purchaseAmount % 10 >= 5:
                price = (purchaseAmount // 10 + 1) * 10
            else:
                price = (purchaseAmount // 10) * 10
        # print("price: ", price)
        return 100 - price

def main(purchaseAmount):
    result = Solution()
    print(result.accountBalanceAfterPurchase(purchaseAmount))

if __name__== "__main__" :
    purchaseAmount = 9
    main(purchaseAmount)
