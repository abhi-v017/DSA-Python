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
    def Insertionat(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            curr = self.head
            prev = None
            while curr is not None and count < position:
                prev = curr
                curr = curr.next
                count+=1
            prev.next = new_node
            new_node.next = curr
    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    del(temp)
                    return
                else:
                    print("value not found!")
                    
        

sll = SinglyLinkedList()

sll.append(1)
sll.append(3)
sll.append(2)
sll.traverse()
sll.delete(3)
sll.traverse()
