# bitwise operation
# For a series of bits, e.g. [1, 1, 0, 1, 1], as long as there is one bit of zero value, then the result of AND operation on this series of bits would be zero.

# 1101 & 1100 => 1100 (common prefix)

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        # bit shift

        shift = 0
        # find the common 1-bits
        while left < right:
            # print("left, right, shift: ", left, right, shift)

            # right shift both numbers by 1 bit
            left = left >> 1
            right = right >> 1
            # count times of shifting
            shift += 1

            # print("left, right, shift: ", left, right, shift)
        
        # once the loop exits, left and right are equal and represent the common prefix.
        # then left shift the common prefix back to its original position by
        return left << shift



        # wrong

        # if left == right:
        #     return left

        # ans = copy.deepcopy(left)
        # print("ans, bin(ans): ", ans, bin(ans))

        # for i in range(left + 1, right + 1):
        #     print("i, bin(i): ", i, bin(i))
        #     # print("ans, bin(ans): ", ans, bin(ans))

        #     # ans &= i
        #     ans = ans & i
        #     # print("---end of iteration---")
        # return ans

def main(left, right):
    result = Solution()
    print(result.rangeBitwiseAnd(left, right))

if __name__== "__main__" :
    left = 1
    right = 2147483647
    main(left, right)
