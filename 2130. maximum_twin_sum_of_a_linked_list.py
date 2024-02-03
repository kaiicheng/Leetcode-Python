from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        ls = []

        def check(node):
            if node is None:
                return
            else:
                ls.append(node.val)
                check(node.next)

        check(head)
        # print("ls: ", ls)

        ans = []
        for i in range(len(ls) // 2):
            ans.append(ls[i] + ls[len(ls) - i - 1])
        
        return max(ans)

def main(head):
    result = Solution()
    print(result.pairSum(head))

if __name__== "__main__" :
    head = [5,4,2,1]
    main(head)
