from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        ans = []
        
        def traverse(node, ans):
            if node is None:
                return
            else:
                ans.append(node.val)
            traverse(node.next, ans)

        traverse(root, ans)
        return ans

def main(head):
    result = Solution()
    print(result.toArray(head))

if __name__== "__main__" :
    head = [1,2,3,4,3,2,1]
    main(head)
