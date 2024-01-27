from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

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

        mi = float("inf")
        for i in range(len(ls) - 1):
            for j in range(i + 1, i + 2):
                # print("i, j: ", i, j)
                # print("ls[i], ls[j]: ", ls[i], ls[j])
                if abs(ls[i] - ls[j]) < mi:
                    mi = abs(ls[i] - ls[j])
        
        return mi

def main(root):
    result = Solution()
    print(result.getMinimumDifference(root))

if __name__== "__main__" :
    root = [1,0,48,None,None,12,49]
    main(root)
