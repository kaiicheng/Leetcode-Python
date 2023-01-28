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
"""

from typing import List

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # return '{0:x}'.format(int(a, 2) + int(b, 2))  # 4
        return '{0:b}'.format(int(a, 2) + int(b, 2))  # 100

def main():
    a, b = "11", "1"
    result = Solution()
    print(result.addBinary(a, b))


if __name__== "__main__" :
    main()