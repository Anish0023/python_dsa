class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    # Function to insert digit at the end
    def append(self, head, value):
        new_node = Node(value)
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head

    # Function to print the list
    def printList(self, head):
        current = head
        while current:
            print(current.data, end='')
            current = current.next
        print()
class Solution:
    def adding(self, node):
        if not node:
            return 1
        carry = self.adding(node.next)
        node.data += carry
        if node.data < 10:
            return 0
        node.data = 0
        return 1
        
    def addOne(self,head):
        #Returns new head of linked List.
        carry = self.adding(head)
        if carry:
            new_head = Node(carry)
            new_head.next = head
            head = new_head
        return head
if __name__ == "__main__":
    ll = LinkedList()
    head = None
    digits = [9, 9, 9]
    for digit in digits:
        head = ll.append(head, digit)
    print("Original number: ", end='')
    ll.printList(head)
    sol = Solution()
    head = sol.addOne(head)
    print("Number after adding one: ", end='')
    ll.printList(head)