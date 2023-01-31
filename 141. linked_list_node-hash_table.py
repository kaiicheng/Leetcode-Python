"""
Approach 1: Hash Table

Intuition

To detect if a list is cyclic, we can check whether a node had been visited before. A natural way is to use a hash table.

Algorithm

We go through each node one by one and record each node's reference (or memory address) in a hash table. If the current node is null, we have reached the end of the list and 
it must not be cyclic. If current node’s reference is in the hash table, then return true.



Complexity analysis

Let n be the total number of nodes in the linked list.

Time complexity : O(n). We visit each of the nnn elements in the list at most once. Adding a node to the hash table costs only O(1) time.

Space complexity: O(n). The space depends on the number of elements added to the hash table, which contains at most nnn elements.
"""
from typing import List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # # use list 
        # nodes_seen = []

        # while head is not None:
        #     if head in nodes_seen:
        #         return True
        #     nodes_seen.append(head)
        #     head = head.next
        #     # print(nodes_seen)
        # return False

        # use set()
        nodes_seen = set()

        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
            # print(nodes_seen)
        return False

def main():
    # head = [3, 2, 0, -4]
    # pos = 1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    # head = ListNode(1)

    result = Solution()
    print(result.hasCycle(head))


if __name__== "__main__" :
    main()