from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        ls = []
        ans = []
        def check(node, val):
            # print("node: ", node)

            if node is None:
                return
            else:
                if node.val == val:
                    ls.append(node)
                    ans.append(node)
                    return
                else:
                    ls.append(node)

            check(node.left, val)
            check(node.right, val)
        
        check(root, val)
        # print("ls: ", ls)
        # print("ans: ", ans)
        # print("---end---")
        if ans == []:
            # print("1!")
            return None
        else:
            # print("2!")
            return ans[0]
        
def main(root, val):
    result = Solution()
    print(result.searchBST(root, val))

if __name__== "__main__" :
    # root = [4,2,7,1,3]
    # val = 5
    root = [4,2,7,1,3]
    val = 2
    main(root, val)
