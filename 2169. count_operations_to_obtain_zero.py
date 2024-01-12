class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        ans = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            ans += 1
            # print("num1, num2: ", num1, num2)
            # print("ans: ", ans)
        return ans

def main(num1, num2):
    result = Solution()
    print(result.countOperations(num1, num2))

if __name__== "__main__" :
    num1 = 2
    num2 = 3
    main(num1, num2)
