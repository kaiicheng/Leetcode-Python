from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        result = 0
        def check(node, cur_mx, cur_mi):
            nonlocal result
            if node is None:
                return
            else:
                # ls.append(node.val)
                # gap.append(abs(mi - node.val))
                result = max(result, abs(cur_mx-node.val), abs(cur_mi-node.val))
                cur_mx = max(cur_mx, node.val)
                cur_mi = min(cur_mi, node.val)
                check(node.left, cur_mx, cur_mi)
                check(node.right, cur_mx, cur_mi)

        check(root, root.val, root.val)
        # print("ls: ", ls)
        # print("gap: ", gap)
        return result
    
def main(root):
    result = Solution()
    print(result.maxAncestorDiff(root))

if __name__== "__main__" :
    root = [8,3,10,1,6,None,14,None,None,4,7,13]
    main(root)
