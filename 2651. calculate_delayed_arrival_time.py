class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        
        ans = arrivalTime + delayedTime
        return ans % 24

def main(arrivalTime, delayedTime):
    result = Solution()
    print(result.findDelayedArrivalTime(arrivalTime, delayedTime))

if __name__== "__main__" :
    arrivalTime = 15
    delayedTime = 5 
    main(arrivalTime, delayedTime)
