from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ls = []
        def check(node):
            if node is None:
                return
            else:
                ls.append(node)
            check(node.next)
        
        check(head)
        # print("ls: ", ls)

        # if len(ls) % 2 == 0:
        #     ans = ls[len(ls) // 2]
        # else:
        #     ans = ls[len(ls) // 2]

        # ans = ls[len(ls) // 2] if len(ls) % 2 != 0 else ls[len(ls) // 2 + 1]

        return ls[len(ls) // 2]



        # output to array
        # arr = [head]
        # while arr[-1].next:
        #     arr.append(arr[-1].next)
        # return arr[len(arr) // 2]



        # fast and slow pointer
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow

    

def main(head):
    result = Solution()
    print(result.middleNode(head))

if __name__== "__main__" :
    head = [1,2,3,4,5,6]
    main(head)
