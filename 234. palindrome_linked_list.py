from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
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
            return True

        # for i in range(len(ls)//2):
        #     if ls[i] == ls[i - len(ls)]

        if len(ls) % 2 == 0:
            first = ls[:len(ls)//2]
            second = ls[len(ls)//2:]
            second = second[::-1]
        elif len(ls) % 2 == 1:
            first = ls[:len(ls)//2 + 1]
            second = ls[len(ls)//2:]
            second = second[::-1]
        # print("first, second: ", first, second)

        if first == second:
            return True
        else:
            return False

def main(head):
    result = Solution()
    print(result.isPalindrome(head))

if __name__== "__main__" :
    head = [1,2,2,1]
    main(head)