from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        # ls = []
        ans = 0
        def check(node):
            nonlocal ans
            if node is None:
                return
            else:
                # ls.append(node.val)
                ans += 1
                check(node.left)
                check(node.right)
        
        check(root)
        # print("ls: ", ls)

        return ans
        # return len(ls)

def main(root):
    result = Solution()
    print(result.countNodes(root))

if __name__== "__main__" :
    root = [1,2,3,4,5,6]
    main(root)
