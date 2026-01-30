class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        if not head:
            return None
        visited = set()
        prev = None
        curr = head
        while curr:
            if curr.data in visited:
                prev.next = curr.next
            else:
                visited.add(curr.data)
                prev = curr
            curr = curr.next
        return head
if __name__ == '__main__':
    # Example usage:
    sol = Solution()
    head = Node(10)
    head.next = Node(12)
    head.next.next = Node(11)
    head.next.next.next = Node(11)
    head.next.next.next.next = Node(12)
    head.next.next.next.next.next = Node(11)
    head.next.next.next.next.next.next = Node(10)

    print("Original list:")
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

    new_head = sol.removeDuplicates(head)

    print("List after removing duplicates:")
    curr = new_head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")