from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        # print("prev: ", prev)

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            # print("prev: ", prev)

        return prev

def main(head):
    result = Solution()
    print(result.reverseList(head))

if __name__== "__main__" :
    head = [1,2,3,4,5]
    main(head)
