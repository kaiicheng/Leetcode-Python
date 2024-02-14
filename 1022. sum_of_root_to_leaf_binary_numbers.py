from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def preorder(r, curr_number):
            nonlocal root_to_leaf
            if r:
                curr_number = (curr_number << 1) | r.val
                # print("curr_number: ", curr_number)

                # If it's a leaf, update the root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += curr_number
                    
                preorder(r.left, curr_number)
                preorder(r.right, curr_number) 
        
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf



        # wrong

        # ans = []
        # temp = []
        # def check(root):
        #     nonlocal temp
        #     if root is None:
        #         # # ans.append(",")
        #         # ans.append(temp)
        #         # temp = []
        #         return
        #     else:
        #         print("root: ", root.val)
        #         temp.append(root.val)
        #         ans.append(root.val)
        #         check(root.left)
        #         check(root.right)

        # check(root)
        # print("ans: ", ans)
        # # print("temp: ", temp)
        # return -1



        # wrong

        # ans = []
        # temp = []
        # def check(root):
        #     if root is None:
        #         # ans.append(",")
        #         ans.append(temp)
        #         # temp = []
        #         return
        #     else:
        #         print("root: ", root.val)
        #         temp.append(root.val)
        #     check(root.left)
        #     check(root.right)

        # check(root)
        # print("ans: ", ans)
        # print("temp: ", temp)
        # return -1

def main(root):
    result = Solution()
    print(result.sumRootToLeaf(root))

if __name__== "__main__" :
    root = [1,0,1,0,1,0,1]
    main(root)
