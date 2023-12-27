# TreeNode can't be equal

# wrong! 
# memory address might differ?
# if temp == key:

# ls = []
# tar = toString(subRoot, ls)
# tar = copy.deepcopy(tar)

from typing import Optional
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def toString(node, ls):
            if node is None:
                ls.append(None)
                return
            else:
                ls.append(node.val)
            toString(node.left, ls)
            toString(node.right, ls)
            return ls

        # print("root: ", root)
        # print("subRoot: ", subRoot)

        ls = []
        tar = toString(subRoot, ls)
        tar = copy.deepcopy(tar)
        print("tar: ", tar)

        include = False

        def check(node, key):
            nonlocal include
            # print("include: ", include)
            if node is None:
                return
            else:
                # print("node: ", node)
                # print("subRoot: ", subRoot)
                # print(toString(subRoot))
                # print("key: ", key)
                # print("toString(node): ", toString(node))
                # print("key: ", key)
                temp_ls = []
                temp = toString(node, temp_ls)
                # print("temp: ", temp)
                if temp == key:
                    # print("true!")
                    include = True
            check(node.left, key)
            check(node.right, key)

        check(root, tar)
        # print("include: ", include)
        if include:
            return True
        else:
            return False

def main(root, subRoot):
    result = Solution()
    print(result.isSubtree(root, subRoot))

if __name__== "__main__" :
    root = [3,4,5,1,2,None,None,None,None,0]
    subRoot = [4,1,2]
    main(root, subRoot)
