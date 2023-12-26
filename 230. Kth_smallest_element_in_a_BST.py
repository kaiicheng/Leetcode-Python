from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ls = []

        def check(node):
            if node is None:
                return
            else:
                ls.append(node.val)
            check(node.left)
            check(node.right)

        check(root)
        ls.sort()
        # print("ls: ", ls)
        return ls[k - 1]
    
def main(root, k):
    result = Solution()
    print(result.kthSmallest(root, k))

if __name__== "__main__" :
    root = [3,1,4,None,2]
    k = 1
    main(root, k)
