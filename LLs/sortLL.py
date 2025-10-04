# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def findmid(head):
            slow, fast = head, head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return prev  # node before middle
        
        def mergeSort(head):
            if not head or not head.next:
                return head
            
            mid = findmid(head)
            right_head = mid.next
            mid.next = None   # split
            
            left_sorted = mergeSort(head)
            right_sorted = mergeSort(right_head)
            
            return merge(left_sorted, right_sorted)
        
        def merge(head1, head2):
            dummy = ListNode(0)
            ptr = dummy
            
            while head1 and head2:
                if head1.val < head2.val:
                    ptr.next = head1
                    head1 = head1.next
                else:
                    ptr.next = head2
                    head2 = head2.next
                ptr = ptr.next
            
            if head1: ptr.next = head1
            if head2: ptr.next = head2
            
            return dummy.next
        
        return mergeSort(head)
if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    z = Solution().sortList(head)
    while z:
        print(z.val)
        z = z.next