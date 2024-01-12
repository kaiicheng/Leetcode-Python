class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        
        # x - t = num + t => 2 * t = x - num => t = x = 2 * t + num
        return 2 * t + num

def main(num, t):
    result = Solution()
    print(result.theMaximumAchievableX(num, t))

if __name__== "__main__" :
    num = 3
    t = 2
    main(num, t)
