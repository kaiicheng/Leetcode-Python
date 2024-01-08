from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        # print("arr: ", arr)
        gap = abs(arr[1] - arr[0])

        for i in range(2, len(arr)):
            # print("arr[i], arr[0]: ", arr[i], arr[0])
            # print("arr[i] - arr[0]: ", arr[i] - arr[0])
            if abs(arr[i] - arr[i - 1]) != gap:
                return False
        return True

def main(arr):
    result = Solution()
    print(result.canMakeArithmeticProgression(arr))

if __name__== "__main__" :
    arr = [3,5,1]
    main(arr)
