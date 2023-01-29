"""
Approach 2: Iteration
Intuition

Start from the root and then at each iteration pop the current node out of the deque. Then do the same checks as in the approach 1 :

    - p and p are not None,

    - p.val is equal to q.val,

and if checks are OK, push the child nodes.



Complexity Analysis

Time complexity : O(N) since each node is visited exactly once.

Space complexity : O(N) in the worst case, where the tree is a perfect fully balanced binary tree, since BFS will have to store at least an entire level of the tree in the queue, 
and the last level has O(N) nodes.
"""

from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self):
        printval = self

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])  # deque imported from collections

        ## Usage of queue       
        # queue = collections.deque()
        # queue.append('a')
        # queue.append('b')
        # queue.append('c')
        # print(queue)  # deque(['a', 'b', 'c'])

        # queue.appendleft('A')
        # queue.appendleft('B')
        # queue.append('C')
        # print(queue)  # deque(['B', 'A', 'a', 'b', 'c', 'C'])

        # print(queue.pop())  # 'C'
        # print(queue.popleft())  # 'B'


        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True

def main():
    # p, q = [1,2,1], [1,1,2]
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)

    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    
    result = Solution()
    print(result.isSameTree(p, q))



if __name__== "__main__" :
    main()