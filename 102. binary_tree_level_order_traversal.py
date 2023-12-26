from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ls = []
        if not root:
            return ls
        
        def check(node, level):
            print("ls, len(ls): ", ls, len(ls))
            # print("node: ", node)
            # print("level: ", level)

            # start the current level
            if len(ls) == level:
                ls.append([])

            # append the current node value
            ls[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                check(node.left, level + 1)
            if node.right:
                check(node.right, level + 1)
            
        check(root, 0)
        return ls


def main(root):
    result = Solution()
    print(result.levelOrder(root))

if __name__== "__main__" :
    root = [3,9,20,None,None,15,7]
    main(root)
