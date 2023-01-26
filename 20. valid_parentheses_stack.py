"""
Approach 1: Stacks

An interesting property about a valid parenthesis expression is that a sub-expression of a valid expression should also be a valid expression. (Not every sub-expression) e.g.

Also, if you look at the above structure carefully, the color coded cells mark the opening and closing pairs of parenthesis. The entire expression is valid, but sub portions of 
it are also valid in themselves. This lends a sort of a recursive structure to the problem. For e.g. Consider the expression enclosed within the two green parenthesis in the diagram 
above. The opening bracket at index 1 and the corresponding closing bracket at index 6.

What if whenever we encounter a matching pair of parenthesis in the expression, we simply remove it from the expression?

Let's have a look at this idea below where remove the smaller expressions one at a time from the overall expression and since this is a valid expression, we would be left with an 
empty string in the end.

The stack data structure can come in handy here in representing this recursive structure of the problem. We can't really process this from the inside out because we don't have an 
idea about the overall structure. But, the stack can help us process this recursively i.e. from outside to inwards.

Let us have a look at the algorithm for this problem using stacks as the intermediate data structure.

Algorithm

Initialize a stack S.
1. Process each bracket of the expression one at a time.
2. If we encounter an opening bracket, we simply push it onto the stack. This means we will process it later, let us simply move onto the sub-expression ahead.
3. If we encounter a closing bracket, then we check the element on top of the stack. If the element at the top of the stack is an opening bracket of the same type, then we pop 
   it off the stack and continue processing. Else, this implies an invalid expression.
4. In the end, if we are left with a stack still having elements, then this implies an invalid expression.
5. We'll have a look a dry run for the algorithm and then move onto the implementation.


Complexity analysis

Time complexity : O(n)O(n)O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack take O(1) time.
Space complexity : O(n)O(n)O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the brackets onto the stack.
 e.g. ((((((((((.

"""

from typing import List

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'
                # print(top_element)

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)
            # print(stack)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


def main():
    s = "()[]{}"
    target = 9
    result = Solution()
    print(result.isValid(s))


if __name__== "__main__" :
    main()