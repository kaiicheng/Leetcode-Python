from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        # sliding window

        sample = "123456789"
        n = 10
        nums = []

        for length in range(len(str(low)), len(str(high)) + 1):
            # print("length: ", length)
            for start in range(n - length):
                # print("start: ", start)
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)
                # else:
                #     break
                # print("nums: ", nums)
        
        return nums



        # wrong

        # ans = []
        # n = str(low)
        # low_len = len(str(low))
        # high_len = len(str(n))

        # while n < high:

def main(low, high):
    result = Solution()
    print(result.sequentialDigits(low, high))

if __name__== "__main__" :
    low = 1000
    high = 13000
    main(low, high)
