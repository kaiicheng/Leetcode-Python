# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        ls = [root.val]
        search(root.left, ls)
        search(root.right, ls)
        ls.sort()
        # print("ls: ", ls)
        ans = float("inf")
        for i in range(1, len(ls)):
          ans = min(ans, ls[i] - ls[i - 1])
        
        return ans
    
def search(node, list):
    print("ls: ", list)
    if node is None:
        return
    else:
        print("node: ", node.val)
        list.append(node.val)
    
    search(node.left, list)
    search(node.right, list)

def main(a):
    result = Solution()
    print(result.minDiffInBST(a))

if __name__== "__main__" :
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    main(root)
