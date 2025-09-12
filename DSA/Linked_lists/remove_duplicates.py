class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def inserathead(self, val): #insert head
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def traverse_forward(self): #traverse
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()
    def removeduplicates(self):
        current = self.head
        while current is not None:
            if current.prev is not None and current.val == current.prev.val:
                if current.prev is self.head:
                    current.prev = None
                    self.head = current
                else:
                    current.prev.prev.next = current
                    current.prev = current.prev.prev
            current = current.next
        return self.head
    
dll = DoublyLinkedList()
dll.inserathead(8)
dll.inserathead(7)
dll.inserathead(6)
dll.inserathead(6)
dll.inserathead(6)
dll.inserathead(5)
dll.inserathead(4)
dll.inserathead(3)
dll.inserathead(3)
dll.inserathead(3)
dll.inserathead(2)
dll.inserathead(1)
dll.traverse_forward()
dll.removeduplicates()
dll.traverse_forward()