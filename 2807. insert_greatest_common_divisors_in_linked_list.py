from typing import Optional
from math import gcd

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # traverse and build linked list again
        # ls = []
        # def check(node):
        #     if node is None:
        #         return
        #     else:
        #         ls.append(node.val)
        #     check(node.next)

        # check(head)
        # # print("ls: ", ls)

        # def build(node, i):
        #     # print("node, i: ", node, i)
        #     if len(ans) - 1 < i:
        #         return
        #     node.next = ListNode(ans[i])
        #     build(node.next, i + 1)

        # start = ListNode(ls[0])

        # if len(ls) == 1:
        #     return start

        # ans = []
        # ans.append(ls[0])
        # for i in range(1, len(ls)):
        #     # ans.append(ls[i - 1])
        #     ans.append(gcd(ls[i - 1], ls[i]))
        #     ans.append(ls[i])
        # # print("ans: ", ans)

        # build(start, 1)
        # return start



        # print("head: ", head)
        ls = []

        def check(node, i):
            # print("i, node: ", i, node)
            # print("head: ", head)
            # print("ls: ", ls)
            if node is None:
                return
            else:
                if i % 2 == 1:
                    # print("!i % 2 == 0!")
                    ls.append(node.val)
                    # print("head: ", head)
                    check(node.next, i + 1)
                elif i % 2 == 0 and node.next is not None:
                    # print("!i % 2 == 1!")
                    ls.append(node.val)
                    g = gcd(node.val, node.next.val)
                    # print("g: ", g)
                    temp = node.next
                    node.next = ListNode(g)
                    node.next.next = temp
                    # print("head: ", head)
                    check(node.next.next, i)                    

        check(head, 0)
        # print("ls: ", ls)
        return head



        # wrong

        # # print("head: ", head)
        # ls = []

        # def check(node, i, pre):
        #     print("i, pre, node: ", i, pre, node)
        #     # print("head: ", head)
        #     # print("ls: ", ls)
        #     if node is None:
        #         return
        #     else:
        #         if i % 2 == 0:
        #             print("!i % 2 == 0!")
        #             ls.append(node.val)
        #             print("head: ", head)
        #             check(node.next, i + 1, node.val)
        #         elif i % 2 == 1 and node.next is not None:
        #             print("!i % 2 == 1!")
        #             ls.append(node.val)
        #             g = gcd(pre, node.val)
        #             print("g: ", g)
        #             temp = node
        #             node = ListNode(g)
        #             node.next = temp
        #             print("head: ", head)
        #             check(node.next.next, i + 1, None)                    

        # check(head, 0, None)
        # print("ls: ", ls)
        # return head

def main(head):
    result = Solution()
    print(result.insertGreatestCommonDivisors(head))

if __name__== "__main__" :
    head = [18,6,10,3]
    main(head)
