# use the nature of binary search tree
# only need to traverse half of tree every round
# look for the split point

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # print("p.val, q.val: ", p.val, q.val)

        def check(node, p_val, q_val):
            # print("node.val: ", node.val)
            if p_val > node.val and q_val > node.val:    
                return check(node.right, p_val, q_val)
            elif p_val < node.val and q_val < node.val:    
                return check(node.left, p_val, q_val)
            else:
                # print("node.val: ", node.val)
                return node

        ans = check(root, p.val, q.val)
        return ans



        # wrong 

        # print("p.val, q.val: ", p.val, q.val)

        # ls_p = []
        # ls_q = []
        # def check(node, ls, tar):
        #     if node is None or node.val == tar:
        #         return
        #     else:
        #         print("node.val, tar: ", node.val, tar)
        #         ls.append(node.val)
        #     check(node.left , ls, tar)
        #     check(node.right , ls, tar)
        
        # check(root, ls_p, p.val)
        # print("---end---")
        # check(root, ls_q, q.val)
        # print("ls_p: ", ls_p)
        # print("ls_q: ", ls_q)

def main(root, p, q):
    result = Solution()
    print(result.lowestCommonAncestor(root, p, q))

if __name__== "__main__" :
    root = [6,2,8,0,4,7,9,None,None,3,5]
    p = 2
    q = 4
    main(root, p, q)
