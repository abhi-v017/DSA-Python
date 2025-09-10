class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CyclicLinkedList:
    def __init__(self):
        self.head = None
    def create_cycle(self, values):
        if not values:
            return None
        self.head = Node(values[0])
        curr = self.head
        # create linear list
        for val in values[1:]:
            curr.next = Node(val)
            curr = curr.next
        curr.next = self.head.next
    def traverse(self, count):
        result = []
        temp = self.head
        steps = 0
        while temp is not None and steps < count:
            result.append(temp.data)
            temp = temp.next
            steps += 1
        return result
    def floydcycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    def startpoint(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
            return slow
    def length(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count = 1
                fast = fast.next
                while slow != fast:
                    fast = fast.next
                    count = count+1
                return count
    
        
    
cll = CyclicLinkedList()
cll.create_cycle([10, 20, 30, 40])
print(cll.traverse(10))
print(cll.floydcycle())
print(cll.startpoint().data)
print(cll.length())