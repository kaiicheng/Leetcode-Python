from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l = 0
        r = len(arr) - 1

        while l < r:
            # mid = (r - l) // 2
            mid = (l + r) // 2
            
            # print("l, r, mid: ", l, r, mid)

            # if arr[mid] > arr[mid + 1]:
            if arr[mid] < arr[mid + 1]:
                # important! need to plus one!
                # l = mid
                l = mid + 1
            # elif arr[mid] < arr[mid + 1]:
            else:
                r = mid
            # if arr[l] <= arr[mi]:
            #     l = mid
            # elif arr[r] >= arr[mid]:
    
        # print("l, r, mid: ", l, r, mid)
        return l



        # binary search

        # left,right=0,len(arr)-1
        # while(left<=right):
        #     mid=(left+right)//2
        #     if arr[mid-1]<=arr[mid] and arr[mid+1]<=arr[mid]:
        #         return mid
        #     elif arr[mid-1]>arr[mid]:
        #         right=mid
        #     else:
        #         left=mid
        # return left
    
def main(arr):
    result = Solution()
    print(result.peakIndexInMountainArray(arr))

if __name__== "__main__" :
    arr = [0,10,5,2]
    main(arr)
