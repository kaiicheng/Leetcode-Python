from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        level_sum = []
        def check(node, level):
            # print("---start of check---")
            # print("node, level: ", node, level)
            # print("level_sum: ", level_sum)
            if node is None:
                return
            else:
                if len(level_sum) < level:
                    for i in range(level - len(level_sum)):
                        # print("i: ", i)
                        level_sum.append(0)
                    # print("level_sum: ", level_sum)

                level_sum[level - 1] = level_sum[level - 1] + node.val
                check(node.left, level + 1)
                check(node.right, level + 1)

        check(root, 1)
        # print("level_sum: ", level_sum)

        if k > len(level_sum):
            return -1
        else:

            for i in range(k - 1):
                level_sum.remove(max(level_sum))

            return max(level_sum)

def main(root, k):
    result = Solution()
    print(result.kthLargestLevelSum(root, k))

if __name__== "__main__" :
    root = [5,8,9,2,1,3,7,4,6]
    k = 2
    main(root, k)
