class Solution:
    def countEven(self, num: int) -> int:
        
        ans = 0
        while num > 0:
            cur = str(num)
            cur_sum = 0
            for i in cur:
                cur_sum += int(i)
            if cur_sum % 2 == 0:
                ans += 1
            num -= 1
        return ans

def main(num):
    result = Solution()
    print(result.countEven(num))

if __name__== "__main__" :
    num = 30
    main(num)
