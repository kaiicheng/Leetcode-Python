"""
Approach 1: Recursion

Intuition

In a preorder traversal, we need to visit the root node first, then all left child nodes, followed by the right child nodes.

We can take the root's left and right subtrees as a subproblem and recursively solve it. Once we have finished visiting all the left child nodes, we can move onto solving 
the right subtree recursively.

Please refer to the following illustration. The number in each node represents the order of traversal.



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

We visit each node once and perform a constant amount of work at each node.

Space complexity: O(n)

The space is taken up by the recursive call stack. Ideally, we are not using any extra space for variables. But the recursion internally uses a call stack that takes up space 
equivalent to the depth of the tree. The max depth of the tree could be O(n) in the worst-case scenario when the tree is skewed.
    
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

        # initialize an empty array answer.
        answer = []
        
        def dfs(node):
            if not node:
                return

            # Visit root first, then the left subtree, then the right subtree.
            answer.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)

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