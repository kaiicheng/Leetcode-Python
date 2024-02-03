from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 2 Passes

        # # Edge case: return None if there is only one node.
        # if head.next == None:
        #     return None
        
        # count = 0
        # p1 = p2 = head
        
        # # First pass, count the number of nodes in the linked list using 'p1'.
        # while p1:
        #     count += 1
        #     p1 = p1.next
        
        # # Get the index of the node to be deleted.
        # middle_index = count // 2
        
        # # Second pass, let 'p2' move toward the predecessor of the middle node.
        # for _ in range(middle_index - 1):
        #     p2 = p2.next
        
        # # Delete the middle node and return 'head'.
        # p2.next = p2.next.next
        # return head



        ls = []
        def check(node):
            if node is None:
                return
            else:
                ls.append(node.val)
                check(node.next)

        check(head)
        # print("ls: ", ls)

        if len(ls) == 1:
            # print("len 1!")
            return None


        if len(ls) == 1:
            ls.remove(ls[-1])
        else:
            mid = len(ls) // 2
            # ls.remove(ls[mid])
            del ls[mid]
        # print("ls: ", ls)

        def build(node, index):
            if index >= len(ls):
                return
            else:
                node.next = ListNode(ls[index])
            build(node.next, index + 1)

        start = ListNode(ls[0])
        build(start, 1)

        return start

def main(head):
    result = Solution()
    print(result.deleteMiddle(head))

if __name__== "__main__" :
    head = [1,3,4,7,1,2,6]
    main(head)
