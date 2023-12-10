from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []

        def check(root, low, high):
            # print("low, high: ", low, high)
            if root is None:
                return
            else:
                print("root: ", root.val)
                if low <= root.val and root.val <= high:
                    ans.append(root.val)
            check(root.left, low, high)
            check(root.right, low, high)
        
        check(root, low, high)

        print("ans: ", ans)
        return sum(ans)

def main(root, low, high):
    result = Solution()
    print(result.rangeSumBST(root, low, high))

if __name__== "__main__" :
    root = [10,5,15,3,7,null,18]
    low = 7
    high = 15
    main(root, low, high)
