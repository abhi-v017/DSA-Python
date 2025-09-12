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
    def removekey(self, key):
        if self.head.next is None and key == self.head.val:
            return None
        temp = self.head
        prev = None
        new_head = self.head
        while temp is not None:
            if temp.val == key:
                if prev is not None:
                    prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = prev
                if temp == new_head:
                    new_head = new_head.next
            else:
                prev = temp
            temp = temp.next


dll = DoublyLinkedList()
dll.inserathead(4)
dll.inserathead(3)
dll.inserathead(3)
dll.inserathead(3)
dll.inserathead(2)
dll.inserathead(2)
dll.inserathead(1)
dll.traverse_forward()
dll.removekey(2)
dll.traverse_forward()