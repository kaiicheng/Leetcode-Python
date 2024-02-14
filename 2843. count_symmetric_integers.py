class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        count = 0
        
        for num in range(low, high + 1):

            num_str = str(num)
            n = len(num_str)
            
            if n % 2 == 1:
                continue
            
            sum1, sum2 = 0, 0
            half = n // 2
            
            for i in range(half):
                sum1 += int(num_str[i])
                sum2 += int(num_str[i + half])
            
            if sum1 == sum2:
                count += 1
        
        return count



        # ans = 0 
        # for x in range(low, high+1): 
        #     s = str(x)
        #     if not len(s) & 1: 
        #         bal = 0 
        #         for i, ch in enumerate(s): 
        #             if i < len(s)//2: bal += int(ch)
        #             else: bal -= int(ch)
        #         if bal == 0: ans += 1
        # return ans

def main(low, high):
    result = Solution()
    print(result.countSymmetricIntegers(low, high))

if __name__== "__main__" :
    low = 1
    high = 100
    main(low, high)
