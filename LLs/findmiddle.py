class Node:
    def __init__(self,val,next_node=None):
        self.value = val
        self.next = next_node

def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next
    return slow
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    z = find_middle(head)
    print(z.value)