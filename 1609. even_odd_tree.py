from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        ls = []
        level = 1
        level_ls = []
        # print("len(level_ls): ", len(level_ls))
        def check(node, level):
            # print("---check start---")
            if node is None:
                return
            else:
                # print("node.val: ", node.val)
                # print("level: ", level)
                ls.append(node.val)
                if level > len(level_ls):
                    for i in range(level - len(level_ls)):
                        level_ls.append([])
                # print("level_ls, len(level_ls): ", level_ls, len(level_ls))
                # print("level_ls[level - 1]: ", level_ls[level - 1])
                temp = level_ls[level - 1]
                temp.append(node.val)
                level_ls[level - 1] = temp
                check(node.left, level + 1)
                check(node.right, level + 1)
        
        check(root, level)
        # print("ls: ", ls)
        # print("level_ls: ", level_ls)

        for i in range(len(level_ls)):
            cur = level_ls[i]
            # print("cur: ", cur)
            if i % 2 == 0:
                for j in range(len(cur)):
                    if cur[j] % 2 != 1:
                        return False
                pre = cur[0]
                for j in range(1, len(cur)):
                    # print("pre, cur[j]: ", pre, cur[j])
                    if pre >= cur[j]:
                        return False
                    pre = cur[j]

            elif i % 2 == 1:
                for j in range(len(cur)):
                    if cur[j] % 2 != 0:
                        return False
                pre = cur[0]
                for j in range(1, len(cur)):
                    if pre <= cur[j]:
                        return False
                    pre = cur[j]
        return True
    
def main(root):
    result = Solution()
    print(result.isEvenOddTree(root))

if __name__== "__main__" :
    root = [1,10,4,3,None,7,9,12,8,6,None,None,2]
    main(root)
