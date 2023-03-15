class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """



def main():
    nums = [2, 0, 50, 12, 11, 15, 7]
    target = 9
    result = Solution()
    print(result.findMissingRanges(nums, target))


if __name__== "__main__" :
    main()