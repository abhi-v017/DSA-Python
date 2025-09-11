class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def inserathead(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insertatend(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def insertatposition(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.inserathead(val)
            return
        else:
            current = self.head
            count = 0
            while current and count < position-1:
                current = current.next
                count+=1
            if current is None:
                print("position out of bound")
            else:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                    current.next = new_node
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()
    def removehead(self):
        if not self.head:
            print("empty list")
        self.head = self.head.next
        self.head.prev = None
    def removelast(self):
        if not self.head:
            print("empty list")
        current = self.head
        while current.next is not None:
            current = current.next
        current.prev.next = None
    def removefromposition(self, position):
        if not self.head:
            return
        if position == 0:
            self.removehead()
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if not current or not current.next:
            self.removelast()
            return
        node_to_remove = current.next
        current.next = node_to_remove.next
        if node_to_remove.next:
            node_to_remove.next.prev = current
dll = DoublyLinkedList()
dll.inserathead(3)
dll.inserathead(2)
dll.inserathead(1)
dll.traverse_forward()
dll.insertatend(5)
dll.traverse_forward()
dll.insertatposition(val=4,position=3)
dll.traverse_forward()
dll.removefromposition(1)
dll.traverse_forward()
dll.removehead()
dll.traverse_forward()
dll.removelast()
dll.traverse_forward()

