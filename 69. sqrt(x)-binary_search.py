"""
Approach 2: Binary Search

Intuition

Let's go back to the interview context. For x≥2 the square root is always smaller than x/2x and larger than 0 : 0<a<x/2.
Since a is an integer, the problem goes down to the iteration over the sorted set of integer numbers. Here the binary search enters the scene.



Algorithm

- If x < 2, return x.

- Set the left boundary to 2, and the right boundary to x / 2.

- While left <= right:

    - Take num = (left + right) / 2 as a guess. Compute num * num and compare it with x:

        - If num * num > x, move the right boundary right = pivot -1

        - Else, if num * num < x, move the left boundary left = pivot + 1

        - Otherwise num * num == x, the integer square root is here, let's return it

- Return right



Complexity Analysis

Time complexity : O(log⁡N).

Let's compute time complexity with the help of master theorem T(N)=aT(N/b)+Θ(N^d). The equation represents dividing the problem up into a subproblems of size N/b in Θ(N^d) time. 
Here at step there is only one subproblem a = 1, its size is a half of the initial problem b = 2, and all this happens in a constant time d = 0. That means that log⁡b(a)=d and hence 
we're dealing with case 2 that results in O(n^(log⁡b(a)*log(⁡d+1)N)) = O(log⁡N) time complexity.

Space complexity : O(1).
"""

from typing import List
from math import e, log

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        # x≥2 the square root is always smaller than x/2 and larger than 0 : 0<a<x/2.
        left, right = 2, x // 2
        
        while left <= right:

            # take num = (left + right) / 2 as a guess. Compute num * num and compare it with x
            pivot = left + (right - left) // 2

            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right

def main():
    x = 4
    result = Solution()
    print(result.mySqrt(x))


if __name__== "__main__" :
    main()