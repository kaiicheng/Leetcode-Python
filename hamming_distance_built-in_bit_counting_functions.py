# Intuition
# Hamming distance is an interesting metric that is widely applied in several domains, e.g. in coding theory for error detection, in information 
# theory for quantifying the difference between strings.

#     The Hamming distance between two integer numbers is the number of positions at which the corresponding bits are different.

# Given the above definition, it might remind one of the bit operation called XOR which outputs 1 if and only if the input bits are different.

#     As a result, in order to measure the hamming distance between x and y, we can first do x XOR y operation, then we simply count the number of bit 
#     1 in the result of XOR operation.

# We now convert the original problem into a bit-counting problem. There are several ways to count the bits though, as we will discuss in the following sections.



# Approach 1: Built-in BitCounting Functions

# Intuition

# First of all, let us talk of the elephant in the room. As one can imagine, we have various built-in functions that could count the bit 1 for us, 
# in all (or at least most of) programming languages. So if this is the task that one is asked in a project, then one should probably just go for it, 
# rather than reinventing the wheel. We given two examples in the following.

# Now, since this is a LeetCode problem, some of you would argue that using the built-in function is like "implementing a LinkedList with LinkedList", 
# which we fully second as well. So no worry, we will see later some fun hand-crafted algorithms for bit counting.



# Complexity Analysis

# Time Complexity: O(1)
# There are two operations in the algorithm. First, we do the XOR operation which takes a constant time.
# Then, we call the built-in bitCount function. In the worst scenario, the function would take O(k) time where kkk is the number of bits for an integer number. 
# Since the Integer type is of fixed size in both Python and Java, the overall time complexity of the algorithm becomes constant, regardless the input numbers.

# Space Complexity: O(1), a temporary memory of constant size is consumed, to hold the result of XOR operation.
# We assume that the built-in function also takes a constant spac

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
        # print(bin(x ^ y))  # 0b101
        return bin(x ^ y).count("1")  # TypeError: must be str, not int

def main():
    x = 1
    y = 4
    result = Solution()
    print(result.hammingDistance(x, y))


if __name__== "__main__" :
    main()