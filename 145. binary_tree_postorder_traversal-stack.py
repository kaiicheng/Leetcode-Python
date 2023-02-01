from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        
        
        # base case...
        if not root: 
            return []
        
        # create an array list to store the solution result
        sol = []
        
        # create an empty stack and push the root node
        bag = [root]
        
        # loop till stack is empty
        while bag:

            # pop a node from the stack
            node = bag.pop()
            sol.append(node.val)

            # push the left child of the popped node into the stack
            if node.left:
                bag.append(node.left)

            # append the right child of the popped node into the stack
            if node.right:
                bag.append(node.right)

        # return the solution list
        return sol[::-1]
    
def main():
    # root = [1,null,2,3]
    root = TreeNode(1)
    root.left = TreeNode(None)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    result = Solution()
    print(result.postorderTraversal(root))


if __name__== "__main__" :
    main()