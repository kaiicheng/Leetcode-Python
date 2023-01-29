"""
Approach 1: Recursion

Intuition

The simplest strategy here is to use recursion. Check if p and q nodes are not None, and their values are equal. If all checks are OK, do the same 
for the child nodes recursively.

"""

from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self):
        printval = self

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True

        # one of p and q is None
        if not q or not p:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)

def main():
    
    # p, q = [1,2,1], [1,1,2]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)

    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    
    result = Solution()
    print(result.isSameTree(p, q))


if __name__== "__main__" :
    main()