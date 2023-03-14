# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        while headA is not None:
            print("headA:", headA.val)
            pB = headB
            while pB is not None:
                print("headB:", pB.val)
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next

        return None


def main():
    # Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    # Output: Intersected at '2'
   
    # listA = ListNode(1)
    # listA.next = ListNode(9)
    # listA.next.next = ListNode(1)
    # listA.next.next.next = ListNode(2)
    # listA.next.next.next.next = ListNode(4)

    # listB = ListNode(3)
    # listB.next = ListNode(2)
    # listB.next.next = ListNode(4)

    # Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    # Output: Intersected at '8'

    listA = ListNode(4)
    listA.next = ListNode(1)
    listA.next.next = ListNode(8)
    listA.next.next.next = ListNode(4)
    listA.next.next.next.next = ListNode(5)

    listB = ListNode(5)
    listB.next = ListNode(6)
    listB.next.next = ListNode(1)
    listB.next.next.next = ListNode(8)
    listB.next.next.next.next = ListNode(4)
    listB.next.next.next.next.next = ListNode(5)

    result = Solution()
    print(result.getIntersectionNode(listA, listB))


if __name__== "__main__" :
    main()