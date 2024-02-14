from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        ls = []
        def check(node):
            if node is None:
                return
            else:
                ls.append(node.val)
            check(node.left)
            check(node.right)

        ls2 = []
        def check2(node2):
            if node2 is None:
                return
            else:
                ls2.append(node2.val)
            check2(node2.left)
            check2(node2.right)

        check(root1)
        # print("ls: ", ls)
        check2(root2)
        # print("ls2: ", ls2)

        for i in range(len(ls)):
            for j in range(len(ls2)):
                if ls[i] + ls2[j] == target:
                    return True
        return False

def main(root1, root2, target):
    result = Solution()
    print(result.twoSumBSTs(root1, root2, target))

if __name__== "__main__" :
    root1 = [2,1,4]
    root2 = [1,0,3]
    target = 5
    main(root1, root2, target)