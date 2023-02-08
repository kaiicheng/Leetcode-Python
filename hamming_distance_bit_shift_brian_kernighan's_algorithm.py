# Approach 3: Brian Kernighan's Algorithm

# Intuition

# In the above approach, one might wonder that "rather than shifting the bits one by one, is there a faster way to count the bits of one ?". And the answer is yes.

#     If we are asked to count the bits of one, as humans, rather than mechanically examining each bit, we could skip the bits of zero in between the bits of one, 
#     e.g. 10001000.

# In the above example, after encountering the first bit of one at the rightmost position, it would be more efficient if we just jump at the next bit of one, 
# skipping all the zeros in between.

# This is the basic idea of the Brian Kernighan's bit counting algorithm, which applies some smart bit and arithmetic operations to clear the rightmost bit of one. 
# Here is the secret recipe.

#     When we do AND bit operation between number and number-1, the rightmost bit of one in the original number would be cleared.

# Based on the above idea, we then can count the bits of one for the input of 10001000 in 2 iterations, rather than 8.



# 1st iteration of the loop: n = 52
# 00110100    &               (n)
# 00110011                    (n-1)
# ~~~~~~~~
# 00110000

# 2nd iteration of the loop: n = 48
# 00110000    &               (n)
# 00101111                    (n-1)
# ~~~~~~~~
# 00100000

# 3rd iteration of the loop: n = 32
# 00100000    &               (n)
# 00011111                    (n-1)
# ~~~~~~~~
# 00000000                    (n = 0)



# Note, according to the online book of Bit Twiddling Hacks, the algorithm was published as an exercise in 1988, in the book of the C Programming Language 2nd Ed. 
# (by Brian W. Kernighan and Dennis M. Ritchie), though on April 19, 2006 Donald Knuth pointed out that this method "was first published by Peter Wegner in 
# CACM 3 (1960), 322. (Also discovered independently by Derrick Lehmer and published in 1964 in a book edited by Beckenbach.)". By the way, one can find many 
# other tricks about bit operations in the aforementioned book.



# Complexity Analysis

# Time Complexity: O(1).
# Similar as the approach of bit shift, since the size (i.e. bit number) of integer number is fixed, we have a constant time complexity.
# However, this algorithm would require less iterations than the bit shift approach, as we have discussed in the intuition.

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
        while xor:
            distance += 1

        # 1st iteration of the loop: n = 52

            # 00110100    &               (n)
            # 00110011                    (n-1)
            # ~~~~~~~~
            # 00110000

            # n(n-1) remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance



def main():
    x = 1
    y = 4
    result = Solution()
    print(result.hammingDistance(x, y))


if __name__== "__main__" :
    main()