class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next
        print()
    def removefromlast(self, n):
        length = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            length+=1
        if length == n:
            self.head = self.head.next
        postion = length - n
        temp = self.head
        count = 1
        while count<postion:
            temp = temp.next
            count+=1
        temp.next = temp.next.next
        return self.head
        
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
sll.append(7)
sll.append(8)
sll.traverse()
sll.removefromlast(3)
sll.traverse()