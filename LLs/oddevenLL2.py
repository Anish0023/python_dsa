from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd_head , even_head =  None , None
        odd_tail , even_tail = None , None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = None   # detach

            if curr.val % 2 == 1:
                if not odd_head:
                    odd_head = odd_tail = curr
                else:
                    odd_tail.next = curr
                    odd_tail = curr
            else:
                if not even_head:
                    even_head = even_tail = curr
                else:
                    even_tail.next = curr
                    even_tail = curr

            curr = next_node

        if odd_tail:
            odd_tail.next = even_head
            return odd_head
        else:
            return even_head
                                        
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