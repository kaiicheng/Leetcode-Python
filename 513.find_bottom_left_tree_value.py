from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        level = 1
        mx_level = -1
        mx = float("-inf")
        left_ls = []

        def check(node, level):
            nonlocal mx_level, mx, left_ls
            # print("node: ", node)
            if node is None:
                return
            else:
                # print("node.val: ", node.val)
                # print("level: ", level)
                # print("left_ls: ", left_ls)
                if level > mx_level:
                    mx_level = level
                    left_ls = []
                    mx = max(mx, node.val)
                if level == mx_level:
                    mx = max(mx, node.val)    
                    left_ls.append(node.val)
                check(node.left, level + 1)
                check(node.right, level + 1)

        check(root, level)
        # print("mx: ", mx)
        # print("left_ls: ", left_ls)
        # print("mx_level: ", mx_level)
        return left_ls[0]

def main(root):
    result = Solution()
    print(result.findBottomLeftValue(root))

if __name__== "__main__" :
    root = [1,2,3,4,None,5,6,None,None,7]
    main(root)
