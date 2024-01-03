# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        ls = []
        def check(node):
            if node is None:
                return
            else:
                check(node.left)
                ls.append(node.val)
                check(node.right)
        
        def build(node, i, end):
            if i == end:
                return
            else:
                node.right = TreeNode(ls[i])
                build(node.right, i + 1, end)

        check(root)
        # print("ls: ", ls)
        
        start = TreeNode(ls[0])
        build(start, 1, len(ls))

        return start

def main(root):
    result = Solution()
    print(result.increasingBST(root))

if __name__== "__main__" :
    root = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    main(root)
