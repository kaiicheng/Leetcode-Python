from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # ls1 = []
        # ls2 = []
        ans1 = []
        ans2 = []

        def check1(node):
            if node is None:
                return
            else:
                if node.left == None and node.right == None:
                    ans1.append(node.val)
                # ls1.append(node.val)
            check1(node.left)
            check1(node.right)
        
        def check2(node):
            if node is None:
                return
            else:
                if node.left == None and node.right == None:
                    ans2.append(node.val)
                # ls2.append(node.val)
            check2(node.left)
            check2(node.right)
        
        check1(root1)
        check2(root2)

        # print("ls1, ls2: ", ls1, ls2)
        # print("ans1, ans2: ", ans1, ans2)

        if ans1 == ans2:
            return True
        else:
            return False

def main(root1, root2):
    result = Solution()
    print(result.leafSimilar(root1, root2))

if __name__== "__main__" :
    root1 = [3,5,1,6,2,9,8,None,None,7,4]
    root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    main(root1, root2)
