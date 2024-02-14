from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        level_sum = [0]

        def check(node, level):
            # print("node, level: ", node, level)
            # print("level_sum: ", level_sum)
            if node is None:
                return
            else:
                if level > len(level_sum):
                    # print("level > len(level_sum)!")
                    # print("level, len(level_sum): ", level, len(level_sum))
                    for i in range(level - len(level_sum)):
                        # print("i: ", i)
                        level_sum.append(0)
                    level_sum[level - 1] = level_sum[level - 1] + node.val
                else:
                    # print("else!")
                    level_sum[level - 1] = level_sum[level - 1] + node.val
                check(node.left, level + 1)
                check(node.right, level + 1)
                # print("level_sum: ", level_sum)

        check(root, 1)
        return level_sum.index(max(level_sum)) + 1

def main(root):
    result = Solution()
    print(result.maxLevelSum(root))

if __name__== "__main__" :
    root = [1,7,0,7,-8,None,None]
    main(root)
