from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        common = list(set(nums1).intersection(nums2))
        # print("common: ", common)

        if min(nums1) == min(nums2):
            if common != []:
                return min(min(common), min(nums1))
        else:
            if common != []:
                return min(int(str(min(min(nums1), min(nums2))) + str(max(min(nums1), min(nums2)))), min(common))
            else:
                return int(str(min(min(nums1), min(nums2))) + str(max(min(nums1), min(nums2))))

def main(nums1, nums2):
    result = Solution()
    print(result.minNumber(nums1, nums2))

if __name__== "__main__" :
    nums1 = [4,1,3]
    nums2 = [5,7]
    main(nums1, nums2)
