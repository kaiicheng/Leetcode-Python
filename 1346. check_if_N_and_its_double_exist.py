from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        ans = False
        for i in range(len(arr)):
            if arr[i] * 2 in arr:
                if arr[i] != 0:
                    ans = True
                    break
                elif arr[i] == 0:
                    if arr.count(0) >= 2:
                        ans = True
                        break
        return ans

def main(arr):
    result = Solution()
    print(result.checkIfExist(arr))

if __name__== "__main__" :
    arr = [10,2,5,3]
    main(arr)
