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
    def reverselist(self):
        if self.head.next is None:
            return self.head
        prev = None
        current = self.head
        while current is not None:
            front = current.next
            current.next = prev
            current.prev = front
            prev = current
            current = front
        self.head = prev

dll = DoublyLinkedList()
dll.inserathead(3)
dll.inserathead(2)
dll.inserathead(1)
dll.traverse_forward()
dll.reverselist()
dll.traverse_forward()