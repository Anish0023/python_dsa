class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None


class Solution:
    def lengthOfLoop(self, head):
        #code here
        visited_nodes = {}
        timer = 0
        curr = head
        while curr:
            if curr in visited_nodes:
                loop_length  = timer - visited_nodes[curr]
                return loop_length
            visited_nodes[curr] = timer
            timer += 1
            curr = curr.next
        return 0
if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next
    print(Solution().lengthOfLoop(head))