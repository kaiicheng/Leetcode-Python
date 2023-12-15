from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swap(node):
            # print("node", node)
            if node is None:
                return
            if node.next is not None:
                temp = node.val
                node.val = node.next.val
                node.next.val = temp
                swap(node.next.next)
        swap(head)
        return head
    
def main(head):
    result = Solution()
    print(result.swapPairs(head))

if __name__== "__main__" :
    head = [1,2,3,4]
    main(head)
