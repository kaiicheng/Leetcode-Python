from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ls = []

        def check(node):
            print("node: ", node)
            if node is None:
                return
            else:
                ls.append(node.val)
            check(node.next)

        check(head)
        print("ls: ", ls)

        if len(ls) == 1:
            if n == 1:
                return ListNode("")

        if len(ls) > 2:
            # print("ls[:-1 * n], ls[-1* n + 1:]: ", ls[:-1 * n], ls[-1* n + 1:])
            # ls = ls[:-1 * n] + ls[-1* n + 1:]
            ls.pop(n * -1)  # remove the element by index
        else:
            if n == 1:
                ls = ls[:-1]
            elif n == 2:
                ls = ls[1:]
        print("ls: ", ls)

        start = ListNode(ls[0])
        def build(node, i):
            # print("node, i: ", node, i)
            if i >= len(ls):
                return
            else:
                node.next = ListNode(ls[i])
            build(node.next, i + 1)
        
        build(start, 1)
        # print("start: ", start)

        return start

def main(head, n):
    result = Solution()
    print(result.removeNthFromEnd(head, n))

if __name__== "__main__" :
    head = [1,2,3,4,5]
    n = 2
    main(head, n)
