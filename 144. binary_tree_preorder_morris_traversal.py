"""
Approach 3: Morris Traversal

    This approach is more of an extension that you wouldn't be expected to come up with in an interview!

Intuition

Here we briefly introduce the Morris Traversal which only takes constant space!

Recall the previous solutions which have O(n) space complexity, let's think about why we need that much space:

Imagine we are in the middle of a traversal, and the current root node root has left and right subtrees. As we finish visiting the last node last of the left subtree, 
we would like to continue visiting the right subtree of root, but how?

This approach takes O(n) space because we need to track all the previous root nodes so that we can always return to each root and visit the right child once we 
have finished visiting its left child!

We can modify the tree in place instead of using extra space. Note that the last node has no right child, so we can let root be its right child! Therefore, whenever we 
finished visiting last, we can just visit its right child and return to root!

For each unvisited node curr, we can find the last node if it exists, so once we finish iterating over the left subtree, we can always return to curr by 
visiting last.right!

Take the following figure as an example of how we can calculate the preorder traversal of root.



Algorithm

    1. Initialize an answer array. We also need two pointers, curr and last. Initialize curr as the root node.

    2. While curr is not NULL, check if it has a left child or not:

        - If it has a left child, let last be the rightmost node of curr's left subtree. Add curr to the answer and modify last's right child as curr.

        - Otherwise, add curr to the answer and move on to curr's right child.

    3. During the iteration, if we visit a node whose right child is curr, it implies that we are currently at the last node of this curr node. We reset last's right child to NULL and move on to curr's right child.

    4. Return answer after the iteration stops.



Complexity Analysis

Let nnn be the number of nodes in the tree.

Time complexity: O(n)

    - There are n−1 edges in a tree (by definition). Each edge is visited at most two times: first, when we find last and second when we traverse the nodes.

    - We visited each node at most 2 times, which takes O(n) time. Refer to the picture below, the colored edges stand for the revisited edges when finding the 
     'last' nodes.

    - When visiting each node, other than traversing edges we do O(1) work, so the time complexity is O(n).

Space complexity: O(1)

In Morris Traversal, we need to track two nodes curr and last which take constant space. Since we take advantage of the right child of some leaf nodes there is no 
need for extra space. 
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

        answer = []
        curr = root
        
        while curr:
            # If there is no left child, go for the right child.
            # Otherwise, find the last node in the left subtree. 
            if not curr.left:
                answer.append(curr.val)
                curr = curr.right
            else:
                last = curr.left
                while last.right and last.right != curr:
                    last = last.right
                    
                # If the last node is not modified, we let 
                # 'curr' be its right child. Otherwise, it means we 
                # have finished visiting the entire left subtree.
                if not last.right:
                    answer.append(curr.val)
                    last.right = curr
                    curr = curr.left
                else:
                    last.right = None
                    curr = curr.right

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