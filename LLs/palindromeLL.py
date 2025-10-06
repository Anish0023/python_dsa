# Definition for singly-linked list.
'''we could use an array to store the values and then check if the array is a palindrome
but that would take O(n) space. Instead we can use the fast and slow pointer technique to find the middle of the linked list
then reverse the second half of the linked list after spliting and compare

you could also make two separate functions for finding the middle and reversing the linked list
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        # find the mid (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #checking the palindrome condition
        left , right = head , prev # prev gives the previous node before slow
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    z = Solution().isPalindrome(head)
    print(z)

