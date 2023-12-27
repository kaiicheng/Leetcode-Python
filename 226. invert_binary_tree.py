from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # ls = []
        # level = []
        def invert(node):
            if node is None:
                return
            else:
                left = invert(node.left)
                right = invert(node.right)
                node.left = right
                node.right = left
            return node

        invert(root)
        # print("root:", root)
        return root
        # print("level: ", level)



        # wrong

        # ls = []
        # # level = []
        # def invert(node):
        #     if node is None:
        #         return
        #     else:
        #         ls.append(node.val)
        #         invert(node.left)
        #         invert(node.right)
        #     # level.append(1)
        
        # invert(root)
        # print("ls:", ls)
        # # print("level: ", level)
    
def main(root):
    result = Solution()
    print(result.invertTree(root))

if __name__== "__main__" :
    root = [4,2,7,1,3,6,9]
    main(root)  # [4,7,2,9,6,3,1]
