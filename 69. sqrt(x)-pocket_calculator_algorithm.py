"""
Integer Square Root

The value aaa we're supposed to compute could be defined as a^2≤x<(a+1)^2. It is called integer square root. From geometrical points of view, 
it's the side of the largest integer-side square with a surface less than x.

Approach 1: Pocket Calculator Algorithm
Before going to the serious stuff, let's first have some fun and implement the algorithm used by the pocket calculators.

Usually a pocket calculator computes well exponential functions and natural logarithms by having logarithm tables hardcoded or by the other means. Hence the 
idea is to reduce the square root computation to these two algorithms as well

x^0.5=e^((1/2)log⁡x)

That's some sort of cheat because of non-elementary function usage but it's how that actually works in a real life.



Complexity Analysis

Time complexity : O(1)\mathcal{O}(1)O(1).

Space complexity : O(1)\mathcal{O}(1)O(1).
"""

from typing import List
from math import e, log

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        print(e**(0.5 * log(x)))

        left = int(e**(0.5 * log(x)))
        right = left + 1

        # (left)^2 < x^2 < (right)^2
        # x = 8. sqrt(x) = 2.82842... => 2
        # x = 4. sqrt(x) = 2. left = 1.999999... =>2

        return left if right * right > x else right

def main():
    x = 4
    result = Solution()
    print(result.mySqrt(x))


if __name__== "__main__" :
    main()