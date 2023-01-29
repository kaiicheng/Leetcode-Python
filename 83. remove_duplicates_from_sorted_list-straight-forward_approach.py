"""
Approach 1: Straight-Forward Approach

Algorithm

This is a simple problem that merely tests your ability to manipulate list node pointers. Because the input list is sorted, we can determine if a node is a duplicate by comparing its 
value to the node after it in the list. If it is a duplicate, we change the next pointer of the current node so that it skips the next node and points directly to the one after the 
next node.



Complexity Analysis

Time complexity : O(n). Because each node in the list is checked exactly once to determine if it is a duplicate or not, the total run time is O(n) where nnn is the 
number of nodes in the list.

Space complexity : O(1). No additional space is used.

"""
from typing import List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        printval = self
        list=[]
        while printval is not None:
            list.append(printval.val)
            printval = printval.next 
        print(list)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head

        while cur != None and cur.next != None:
            # while cur.next != None and cur.val == cur.next.val:
            #     cur.next = cur.next.next
            # cur = cur.next

            # alternative
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head

def main():
    # head = [1,1,2,3,3]
    list = ListNode(1)
    list.next = ListNode(1)
    list.next.next = ListNode(2)
    list.next.next.next = ListNode(3)
    list.next.next.next.next = ListNode(3)

    # head = [1,1,2,3,3]
    
    # list = ListNode(head[0])

    # for i in range(len(head)):
    #     # list.display()
    #     if i == 0:
    #         pass
    #     else:
    #         list.next = ListNode(head[i])
    #         list = list.next

    # list.display()

    result = Solution().deleteDuplicates(list)
    # print("output: ", end="")
    result.display()


if __name__== "__main__" :
    main()