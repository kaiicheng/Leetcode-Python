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



Approach 1: Bit-by-Bit Computation
Algorithm

That's a good old classical algorithm, and there is no conversion from binary string to decimal and back here. Let's consider the numbers bit by bit starting from the 
lowest one and compute the carry this bit will add.

Start from carry = 0. If number a has 1-bit in this lowest bit, add 1 to the carry. The same for number b: if number b has 1-bit in the lowest bit, add 1 to the carry. 
At this point the carry for the lowest bit could be equal to (00)2, (01)2, or (10)2.

Now append the lowest bit of the carry to the answer, and move the highest bit of the carry to the next order bit.

Repeat the same steps again, and again, till all bits in a and b are used up. If there is still nonzero carry to add, add it. Now reverse the answer string and 
the job is done.



Complexity Analysis

Time complexity: O(max⁡(N,M)), where N and M are lengths of the input strings a and b.

Space complexity: O(max⁡(N,M)) to keep the answer.
"""

from typing import List

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        # str = "this is string example....wow!!!";
        # print str.zfill(40);  # 00000000this is string example....wow!!!
        # print str.zfill(50);  # 000000000000000000this is string example....wow!!!

        # a, b = "11", "1"

        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)  # a = 11, b = 01

        carry = 0
        answer = []

        for i in range(n - 1, -1, -1):  # n-1, n-2, n-3, ..., 1, 0

            if a[i] == '1':
                carry += 1
            
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')

            carry //= 2

        # add one more digit at the beginning, if carry is necessary
        if carry == 1:
            answer.append('1')

        answer.reverse()

        # Usage of .join()

        # symbol = "-"
        # seq = ("a", "b", "c")
        # print (symbol.join(seq))  # a-b-c

        # myTuple = ("Bill", "Steve", "Elon")
        # x = "".join(myTuple)
        # print(x)

        return ''.join(answer)

def main():
    a, b = "11", "1"
    result = Solution()
    print(result.addBinary(a, b))


if __name__== "__main__" :
    main()