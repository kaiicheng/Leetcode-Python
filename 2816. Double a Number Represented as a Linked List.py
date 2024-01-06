from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # without using sys
        # sys.set_int_max_str_digits(100000)
        
        num = 0
        while head:
            num = num * 10 + head.val
            head = head.next

        num *= 2

        dummy = ListNode()
        curr = dummy

        digits = []
        if num == 0:
            digits = [0]
        while num > 0:
            digits.append(num % 10)
            num //= 10

        for digit in reversed(digits):
            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next



        # ls = []

        # def check(node):
        #     if node is None:
        #         return
        #     else:
        #         ls.append(str(node.val))
        #         # ls.append(node.val)
        #         check(node.next)
        
        # check(head)
        # # print("ls: ", ls)

        # # ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 4590 digits; use sys.set_int_max_str_digits() to increase the limit
        # sys.set_int_max_str_digits(100000)
        # double = int("".join(ls)) * 2


        # # double = 0
        # # for i in range(len(ls)):
        # #     # print("i, ls[i], len(ls) - i - 1: ", i, ls[i], len(ls) - i - 1)
        # #     # print("ls[i] * (len(ls) - i - 1) * 10: ", ls[i] * (len(ls) - i - 1) * 10)
        # #     double += ls[i] * 10 ** (len(ls) - i - 1)
        # # double *= 2
        # # print("double: ", double)

        # ls = [int(i) for i in str(double)]
        # def build(node, ls, i):
        #     if len(ls) <= i:
        #         return
        #     else:
        #         node.next = ListNode(ls[i])
        #         build(node.next, ls, i + 1)

        # start = ListNode(ls[0])
        # build(start, ls, 1)

        # return start

def main(head):
    result = Solution()
    print(result.doubleIt(head))

if __name__== "__main__" :
    head = [9,9,9]
    main(head)
