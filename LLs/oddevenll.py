from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        to reduce O(n) space complexity we can just break the links between odd and even nodes
        take first node , previously its link is with even node so we change it
            odd.next = even.next
            even.next = even.next.next
        to merge the odd by even we need to keep track of the even head so that we simply perform
            odd.next = even.head 
        '''
        if not head or not head.next:
            return head
        odd , even = head , head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head
    def  printList(self, head):
        while head:
            print(head.val,'->', end=' ')
            head = head.next
if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print('Before')
    Solution().printList(head)
    head = Solution().oddEvenList(head)
    print('After')
    Solution().printList(head)
