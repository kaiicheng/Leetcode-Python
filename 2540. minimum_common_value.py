from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        s1 = set(nums1)
        s2 = set(nums2)

        ans = []
        for i in s1:
            if i in s2:
                ans.append(i)
        
        if len(ans) == 0:
            return -1
        else:
            return min(ans)

def main(nums1, nums2):
    result = Solution()
    print(result.getCommon(nums1, nums2))

if __name__== "__main__" :
    nums1 = [1,2,3]
    nums2 = [2,4]
    main(nums1, nums2)
