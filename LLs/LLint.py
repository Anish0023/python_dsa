class Node:
    def __init__(self , data=None, next= None):
        self.data = data
        self.next = next
    def setData(self,data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next != None

class LinkedList(object):
    def __init__(self, node = None):
        self.length = 0
        self.head = None
    
    def length(self):
        curr = self.head
        cnt = 0
        while curr:
            cnt += 1
            curr = curr.next
        return cnt
          
    