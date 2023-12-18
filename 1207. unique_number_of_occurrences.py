from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        di = {}
        for i in range(len(arr)):
            if arr[i] not in di:
                di[arr[i]] = 1
            else:
                di[arr[i]] += 1
        print("di: ", di)

        ls = list(di.values())
        print("ls: ", ls)
        ls.sort()

        for i in range(len(ls) - 1):
            if ls[i] == ls[i + 1]:
                return False
        return True

def main(arr):
    result = Solution()
    print(result.uniqueOccurrences(arr))

if __name__== "__main__" :
    arr = [1,2,2,1,1,3]
    main(arr)
