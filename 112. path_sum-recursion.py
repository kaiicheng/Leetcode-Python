"""
Binary tree definition
First of all, here is the definition of the TreeNode which we would use in the following implementation.

class TreeNode(object):
    # Definition of a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

Approach 1: Recursion

The most intuitive way is to use a recursion here. One is going through the tree by considering at each step the node itself and its children. If node is not a leaf, 
one calls recursively hasPathSum method for its children with a sum decreased by the current node value. If node is a leaf, one checks if the the current sum is zero, i.e 
if the initial sum was discovered.



Complexity Analysis

Time complexity : we visit each node exactly once, thus the time complexity is O(N), where NNN is the number of nodes.
Space complexity : in the worst case, the tree is completely unbalanced, e.g. each node has only one child node, the recursion call would occur NNN times (the height of the tree), 
therefore the storage to keep the call stack would be O(N). But in the best case (the tree is completely balanced), the height of the tree would be log⁡(N). Therefore, the space 
complexity in this case would be O(log⁡(N)).
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

        sum -= root.val

        # if reach a leaf
        if not root.left and not root.right:
            return sum == 0

        # return True, if any one with case of sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

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