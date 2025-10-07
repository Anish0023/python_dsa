# Definition for singly-linked list.
'''we can use insertion sort to sort the linked list
we can use a dummy node to help us with the insertion
we can use two pointers, one to keep track of the previous node and one to keep track of the current node
if the current node is greater than the previous node, we can move both pointers forward
if the current node is less than the previous node, we can find the correct position to insert the current node by iterating from the dummy node
we can then insert the current node at the correct position and update the pointers accordingly
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev, cur = head , head.next

        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue
            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
        return dummy.next
if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    z = Solution().insertionSortList(head)
    while z:
        print(z.val)
        z = z.next

        

        