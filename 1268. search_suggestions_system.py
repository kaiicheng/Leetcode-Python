from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        # print("products: ", products)

        ls = []
        ans = []
        for i in range(1, len(searchWord) + 1):
            cur = searchWord[:i]
            # print("cur: ", cur)

            temp = []
            # print("min(len(products), 3): ", min(len(products), 3))
            for j in range(len(products)):
                # temp.append(products[j])
                # print("j, products[j]: ", j, products[j])
                # print("products[j].find(cur: ", products[j].find(cur))
                if cur in products[j] and products[j].find(cur) == 0:
                    temp.append(products[j])
                if len(temp) == min(3, len(products)):
                    break
            ans.append(temp)
            # print("temp: ", temp)

        # print("ans: ", ans)

        return ans

def main(products, searchWord):
    result = Solution()
    print(result.suggestedProducts(products, searchWord))

if __name__== "__main__" :
    products = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord = "mouse"
    main(products, searchWord)
