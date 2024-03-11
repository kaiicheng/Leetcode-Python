from typing import Optional 
from collections import Counter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ls = []
        def check(node):
            if node is None:
                return 
            else:
                ls.append(node.val)
                check(node.next)
        
        check(head)
        c = Counter(ls)
        freq = c.values()
        freq = list(freq)
        # print("freq: ", freq)

        start_head = ListNode(freq[0])
        start = start_head
        for i in range(1, len(freq)):
            # print("i, freq[i]: ", i, freq[i])
            start.next = ListNode(freq[i])
            start = start.next

        return start_head

def main(head):
    result = Solution()
    print(result.frequenciesOfElements(head))

if __name__== "__main__" :
    head = [1,1,2,2,2] 
    main(head)
