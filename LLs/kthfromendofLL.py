class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    # Function to insert a new node at the end
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
            print(current.data, end=' ')
            current = current.next
        print()

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def getKthFromLast(self, head, k):
        #code here
        head = self.reverse(head)
        curr = head
        i = 0
        while i != k-1 and curr :
            i += 1
            curr = curr.next
           
        if curr:
            return curr.data
        else:
            return -1
if __name__ == "__main__":
    ll = LinkedList()
    head = None
    values = [10, 20, 30, 40, 50]
    for value in values:
        head = ll.append(head, value)
    print("Linked List: ", end='')
    ll.printList(head)
    k = 2
    sol = Solution()
    kth_value = sol.getKthFromLast(head, k)
    print(f"{k}th node from the end is: {kth_value}")