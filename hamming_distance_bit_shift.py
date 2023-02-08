# Intuition

# In order to count the number of bit 1, we could shift each of the bit to either the leftmost or the rightmost position and then check if the bit 
# is one or not.

# More precisely, we should do the logical shift where zeros are shifted in to replace the discarded bits.

# Here we adopt the right shift operation, where each bit would has its turn to be shifted to the rightmost position. Once shifted, we then check if the 
# rightmost bit is one, which we can use either the modulo operation (i.e. i % 2) or the bit AND operation (i.e. i & 1). Both operations would mask out 
# the rest of the bits other than the rightmost bit.



# Complexity Analysis

# Time Complexity: O(1), since the Integer is of fixed size in Python and Java, the algorithm takes a constant time. 
# For an Integer of 32 bit, the algorithm would take at most 32 iterations.

# Space Complexity: O(1), a constant size of memory is used, regardless the input.

from typing import List

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # print(x)  # 1
        # print(bin(x))  # 0b1 => 0b0001
        # print(y)  #4
        # print(bin(y))  #0b100
        # print(bin(x ^ y))  # 0b101 => 5

        xor = x ^ y  # 0b101 => 5
        distance = 0

        # five = 5
        # while five:
        #     five -= 1
        #     print(five)  # 4, 3, 2, 1, 0

        # check every digit is different or not
        while xor:  # while 0 => False. while 5 => True
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance



def main():
    x = 1
    y = 4
    result = Solution()
    print(result.hammingDistance(x, y))


if __name__== "__main__" :
    main()