# default low and high threshold

# def check(node, low=float("-inf"), high=float("inf")):
#     nonlocal false

#     if false:
#         return

#     if node is None:
#         return
#     else:
#         if node.val <= low or node.val >= high:
#             false = True
#     check(node.left, low, node.val)
#     check(node.right, node.val, high)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ls = []
        false = False

        def check(node, low=float("-inf"), high=float("inf")):

            nonlocal false
            # global false

            if false:
                return

            # print("node: ", node)

            if node is None:
                # print("0!")
                return
            # elif node is not None and node.left is None and node.right is None:
            #     return
            else:
                if node.val <= low or node.val >= high:
                    false = True
                    # return False

                # print("node, node.left, node.right: ", node, node.left, node.right)
                # ls.append(node.val)
                # if node.left is not None:
                #     if node.left.val >= node.val:
                #         # print("1!")
                #         false = True
                # if node.right is not None:
                #     if node.val >= node.right.val:
                #         # print("2!")
                #         false = True
                # else:
                #     print("3!")
                #     false = True
                    # return False
            # print("false: ", false)
            check(node.left, low, node.val)
            check(node.right, node.val, high)

        check(root)
        # print("ls: ", ls)
        # print("false: ", false)

        if false:
            return False
        else:
            return True

def main(root):
    result = Solution()
    print(result.isValidBST(root))

if __name__== "__main__" :
    root = [2,1,3]
    main(root)
