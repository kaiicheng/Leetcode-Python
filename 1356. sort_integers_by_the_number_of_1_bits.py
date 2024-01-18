from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        arr.sort()

        ls = []
        for i in range(len(arr)):
            ls.append([bin(arr[i]).count("1"), arr[i]])
        ls.sort()

        # print("ls: ", ls)
        ans = [i[1] for i in ls]
        return ans

def main(arr):
    result = Solution()
    print(result.sortByBits(arr))

if __name__== "__main__" :
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    main(arr)
