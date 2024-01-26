# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        ls = []

        def check(node):
            if node is None:
                return
            else:
                ls.append(node.val)
            check(node.left)
            check(node.right)
        
        def build(node):
            if node is None:
                return
            else:
                # print("node, node.val: ", node, node.val)
                temp = [i for i in ls if i >= node.val]
                node.val = sum(temp)
                # print("node.val: ", node.val)
                build(node.left)
                build(node.right)

        check(root)
        build(root)

        return root

def main(root):
    result = Solution()
    print(result.bstToGst(root))

if __name__== "__main__" :
    root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    main(root)
