"""
Overview

There is a simple way using built-in functions:

Convert a and b into integers.

Compute the sum.

Convert the sum back into binary form.

class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

Usage of .format():

    "{} {}".format("hello", "world")
    'hello world'
    
    "{0} {1}".format("hello", "world")
    'hello world'
    
    "{1} {0} {1}".format("hello", "world")
    'world hello world'

Usage of int():

x = "10"
num1 = int(x, 2)
num2 = int(x, 8)
num3 = int(x, 16)
print(num1)  # 2 = 2^1
print(num2)  # 8 = 8^1
print(num3)  # 16 = 16^1



The overall algorithm has O(N+M) time complexity and has two drawbacks which could be used against you during the interview.

1 . In Java this approach is limited by the length of the input strings a and b. Once the string is long enough, the result of conversion into integers 
    will not fit into Integer, Long or BigInteger:

    - 33 1-bits - and b doesn't fit into Integer.

    - 65 1-bits - and b doesn't fit into Long.

    - 500000001 1-bits - and b doesn't fit into BigInteger.

To fix the issue, one could use standard Bit-by-Bit Computation approach which is suitable for quite long input strings.

2 . This method has quite low performance in the case of large input numbers.

One could use Bit Manipulation approach to speed up the solution.



Approach 2: Bit Manipulation

Intuition

Here the input is more adapted to push towards Approach 1, but there is popular Facebook variation of this problem when interviewer provides you two numbers and asks 
to sum them up without using addition operation.

    No addition? OK, bit manipulation then.

How to start? There is an interview tip for bit manipulation problems: if you don't know how to start, start from computing XOR for your input data. Strangely, 
that helps to go out for quite a lot of problems, Single Number II, Single Number III, Maximum XOR of Two Numbers in an Array, Repeated DNA Sequences, Maximum Product 
of Word Lengths, etc.

Here XOR is a key as well, because it's a sum of two binaries without taking carry into account.

To find current carry is quite easy as well, it's AND of two input numbers, shifted one bit to the left.

Now the problem is reduced: one has to find the sum of answer without carry and carry. It's the same problem - to sum two numbers, and hence one could solve it in a 
loop with the condition statement "while carry is not equal to zero".



Algorithm

Convert a and b into integers x and y, x will be used to keep an answer, and y for the carry.

While carry is nonzero: y != 0:

Current answer without carry is XOR of x and y: answer = x^y.

Current carry is left-shifted AND of x and y: carry = (x & y) << 1.

Job is done, prepare the next loop: x = answer, y = carry.

Return x in the binary form.



Performance Discussion

Here we deal with input numbers which are greater than 2^100. That forces to use slow BigInteger in Java, and hence the performance gain will be present 
for the Python solution only. Provided here Java solution could make its best with Integers or Longs, but not with BigIntegers.



Complexity Analysis

Time complexity : O(N+M), where NNN and MMM are lengths of the input strings a and b.

Space complexity : O(max⁡(N,M)) to keep the answer.
"""

from typing import List

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # Concept
        # If we take XOR of zero and some bit, it will return that bit
        # a⊕0=a
        # If we take XOR of two same bits, it will return 0
        # a⊕a=0

        # a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        # So we can XOR all bits together to find the unique number.

        # XOR:
        # 0^0 ->0
        # 1^0 ->1
        # 0^1 ->1
        # 1^1 ->0

        # 5 = 0101(b)
        # 3 = 0011(b)
        # 5 ^ 3 => 6 (0110(b))

        # print(5^5)  # 0
        # print(6^6)  # 0
        # same value x^x always lead to 0

        x, y = int(a, 2), int(b, 2)  # x= 3, y = 1

        while y:  # when y > 0, y is true

            # only record the digit with different values
            answer = x ^ y  # ^ => XOR
            # 1 1
            # 0 1
            #-----
            # 1 0

            # 1 0
            # 1 0
            #-----
            # 0 0

            # only record the digit with same value and shift left by one digit
            carry = (x & y) << 1
            # 1 1
            # 0 1
            #-----
            # 0 1  << 1
            # 1 0

            # 1 0
            # 1 0
            #-----
            # 1 0  << 1
            # 1 0 0

            x, y = answer, carry

        # print(x)  # 4

        # return x in the binary form.
        # return bin(x)[:]  # 0b100
        return bin(x)[2:]  # 100
    
        # # alternative
        # x, y = int(a, 2), int(b, 2)
        # while y:
        #     x, y = x ^ y, (x & y) << 1
        # return bin(x)[2:]

def main():
    a, b = "11", "1"
    result = Solution()
    print(result.addBinary(a, b))


if __name__== "__main__" :
    main()