class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # check if they have non-zero GCD string
        if str1 + str2 != str2 + str1:
            return ""

        # get the gcd of the two lengths
        print("gcd(len(str1), len(str2)): ", gcd(len(str1), len(str2)))
        max_length = gcd(len(str1), len(str2))

        return str1[:max_length]
    
def main(str1, str2):
    result = Solution()
    print(result.gcdOfStrings(str1, str2))

if __name__== "__main__" :
    str1 = "ABCABC"
    str2 = "ABC"
    main(str1, str2)
