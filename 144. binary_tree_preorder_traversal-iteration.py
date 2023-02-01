"""
Approach 2: Iteration

Intuition

We can also implement DFS iteratively using a stack to replicate recursive calls. Note that the operations on the stack follow the first-in-last-out order. 
The node we add last is visited first. Therefore, to access the left child before the right child, we add the right child before the left child.



Algorithm

    1. Initialize an empty array answer and an empty stack stack.

    2. Add root to stack.

    3. While stack is not empty, get the top node currNode from stack. If currNode is not NULL:

        - add its value to answer.
        - add its right child to stack.
        - add its left child to stack.
    Then repeat step 3.

    4. Return answer after we empty stack.


Algorithm
    1. Initialize an empty array answer.
    2. Start with the root node root. If root is not NULL:
        - add its value to answer.
        - repeat step 2 with root's left child
        - repeat step 2 with root's right child.
    3. Return answer after the iteration stops.



Complexity Analysis

Let n be the number of nodes in the tree.

Time complexity: O(n)

We use a stack to store all nodes to be visited. Each of the n nodes is added to and popped from the stack once, which takes O(1) time.

All other work done at each node is O(1), so the overall time complexity is O(n).

Space complexity: O(n)

We use a stack to store all the nodes to be visited. Similar to the previous approach, the stack takes up space equivalent to the depth of the tree. The max depth of the
tree could be O(n) in the worst-case scenario when the tree is skewed.
"""
from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # initialize an empty array answer and an empty stack stack
        answer = []
        stack = [root]

        # while stack is not empty, get the top node currNode from stack
        while stack:

            curr_node = stack.pop()
            
            # base case
            if curr_node:
                
                # add its value to answer
                answer.append(curr_node.val)

                # note that we add curr_node's right child to the stack first
                stack.append(curr_node.right)
                stack.append(curr_node.left)

        # return answer after we empty stack
        return answer

def main():
    # root = [1,null,2,3]
    root = TreeNode(1)
    root.left = TreeNode(None)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    result = Solution()
    print(result.preorderTraversal(root))


if __name__== "__main__" :
    main()