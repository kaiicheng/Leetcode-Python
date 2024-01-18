class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        step = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            elif num % 2 == 1:
                num -= 1
            step += 1
        return step

def main(num):
    result = Solution()
    print(result.numberOfSteps(num))

if __name__== "__main__" :
    num = 14
    main(num)
