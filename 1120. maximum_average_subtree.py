from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        ls = []
        ls_avg = []
        def check(node):
            nonlocal cur, length
            # print("---start check function---")
            # print("node: ", node)
            if node is None:
                return 
            else:
                avg(node)

                # print("cur, length[0]: ", cur, length[0])
                ls_avg.append(sum(cur)/length[0])
                cur = []
                length = [0]


                ls.append(node.val)
                check(node.left)
                check(node.right)
                # print("---end check function---")

        length = [0]
        cur = []
        def avg(root):
            nonlocal cur, length
            # print("-start avg function-")
            # print("root, length: ", root, length)
            # print("cur: ", cur)
            if root is None:
                return
            else:
                length[0] = length[0] + 1
                cur.append(root.val)
                avg(root.left)
                avg(root.right)
                # print("cur: ", cur)
                # print("-end avg function-")


        check(root)
        # print("ls: ", ls)
        # print("ls_avg: ", ls_avg)
        return max(ls_avg)
    
def main(root):
    result = Solution()
    print(result.maximumAverageSubtree(root))

if __name__== "__main__" :
    root = [5,6,1]
    main(root)