'''
Docstring for LLs.removeduplicatesfromsortedlist2
We want to remove all duplicate nodes entirely from a sorted linked list, keeping only nodes that appear exactly once. A dummy node helps us handle edge cases where duplicates occur at the start.

🧠 Approach
Use a dummy node pointing to the head.
Traverse the list using two pointers: prev (last confirmed unique node) and cur (current node being inspected).
If cur.val == cur.next.val, skip all nodes with the same value.
Otherwise, move prev forward.
Return the list starting from dummy.next.

'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next  # Skip all duplicates
            else:
                prev = prev.next  # Move to next distinct node
            cur = cur.next

        return dummy.next
    def print(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
# Driver code to test the Solution
if __name__ == '__main__':
    sol = Solution()
    # Example usage:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    print("Original list:")
    sol.print(head)
    new_head = sol.deleteDuplicates(head)
    # Print the resulting linked list
    sol.print(new_head)
