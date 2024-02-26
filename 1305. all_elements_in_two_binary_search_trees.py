from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        ls = []
        def check(node):
            # print("ls: ", ls)
            if node is None:
                return
            else:
                ls.append(node.val)
                check(node.left)
                check(node.right)

        check(root1)
        check(root2)

        ls.sort()
        # print("ls: ", ls)

        return ls

def main(root1, root2):
    result = Solution()
    print(result.getAllElements(root1, root2))

if __name__== "__main__" :
    root1 = [2,1,4]
    root2 = [1,0,3]
    main(root1, root2)
