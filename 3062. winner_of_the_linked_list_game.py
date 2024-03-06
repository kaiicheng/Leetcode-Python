from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        
        ls = []

        def check(node):
            if node is None:
                return
            else:
                ls.append(node.val)
                check(node.next)

        check(head)
        # print("ls: ", ls)

        even = 0
        odd = 0
        for i in range(0, len(ls), 2):
            # print("i: ", i)
            if ls[i] > ls[i + 1]:
                even += 1
            else:
                odd += 1

        # print("even, odd: ", even, odd)

        if odd > even:
            return "Odd"
        elif odd < even:
            return "Even"
        elif odd == even:
            return "Tie"

def main(head):
    result = Solution()
    print(result.gameResult(head))

if __name__== "__main__" :
    head = [2,5,4,7,20,5]
    main(head)
