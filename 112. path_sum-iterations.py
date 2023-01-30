"""
Approach 2: Iterations
Algorithm

We could also convert the above recursion into iteration, with the help of stack. DFS would be better than BFS here since it works faster except the worst case. In the worst case 
the path root->leaf with the given sum is the last considered one and in this case DFS results in the same productivity as BFS.

The idea is to visit each node with the DFS strategy, while updating the remaining sum to cumulate at each visit.

So we start from a stack which contains the root node and the corresponding remaining sum which is sum - root.val. Then we proceed to the iterations: pop the current node out of 
the stack and return True if the remaining sum is 0 and we're on the leaf node. If the remaining sum is not zero or we're not on the leaf yet then we push the child nodes and corresponding remaining sums into stack.


Complexity Analysis

Time complexity : the same as the recursion approach O(N).
Space complexity : O(N) since in the worst case, when the tree is completely unbalanced, e.g. each node has only one child node, we would keep all NNN nodes in the stack. But in the 
best case (the tree is balanced), the height of the tree would be log⁡(N). Therefore, the space complexity in this case would be O(log⁡(N)).
"""

from typing import List

class TreeNode(object):
    # Definition of a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        # avoid empty tree
        # root = [], targetSum = 0 => False
        if not root:
            return False

        # use a list as stack
        stack = [(root, sum - root.val), ]

        while stack:
            
            # pop the last element from the stack
            node, curr_sum = stack.pop()
            # print(node)  # <__main__.TreeNode object at 0x000002065B720FD0>

            # base case, reach a leaf and with sum == 0
            if not node.left and not node.right and curr_sum == 0:  
                return True

            # push the right node to stack, if exist
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            # push the left node to stack, if exist
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))

        return False

def main():
  
    # root = [1,2,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    targetSum = 5
    result = Solution()
    print(result.hasPathSum(root, targetSum))


if __name__== "__main__" :
    main()