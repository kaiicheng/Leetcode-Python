class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        title = ""
        while columnNumber > 0:
            columnNumber -= 1  # 27. 700, 25

            # ASCII code for the letter "A" is 65
            # chr(65) = A, chr(66) = B

            # 1. check the residual number

            # chr(27 % 26 + 65) + "" = B
            # chr(1%26 + 65) + "B" = AB

            # chr(700 % 26 + 65) = Y
            # chr(25 % 26 + 65) + "Y" = ZY
            title = chr(columnNumber % 26 + 65) + title
            
            # 2. calculate how many 26 the number has
            columnNumber //= 26  # 27 //= 26 => 1. 700//26 = 26

        return title



def main():
    # nums = 28
    # nums = 701
    nums = 53
    result = Solution()
    print(result.convertToTitle(nums))


if __name__== "__main__" :
    main()