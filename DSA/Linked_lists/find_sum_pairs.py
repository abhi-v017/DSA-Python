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
    def pairsum(self, target):
        my_set = set()
        result = []
        temp = self.head
        while temp is not None:
            remaining = target - temp.val
            if remaining in my_set:
                result.append([remaining, temp.val])
                my_set.add(temp.val)
            else:
                my_set.add(temp.val)
            temp = temp.next
        return result
    def pairsumsecond(self, target):
        result = []
        right = self.head
        while right.next is not None:
            right = right.next
        left = self.head
        while left is not None and right is not None and left.val<right.val:
            total = left.val + right.val
            if total==target:
                result.append([left.val, right.val])
                left = left.next
                right = right.prev
            elif total>target:
                right = right.prev
            else:
                left = left.next
        return result
                
dll = DoublyLinkedList()
dll.inserathead(8)
dll.inserathead(7)
dll.inserathead(6)
dll.inserathead(5)
dll.inserathead(4)
dll.inserathead(3)
dll.inserathead(2)
dll.inserathead(1)
dll.traverse_forward()
print(dll.pairsum(8))
print(dll.pairsumsecond(8))