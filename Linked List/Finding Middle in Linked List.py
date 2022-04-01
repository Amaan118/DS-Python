# Finding Middle of Linked List in One Pass

class Create_Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next

class LinkedList:
    def __init__(self, val):
        self.head = Create_Node(val)
    
    def insert_at_begin(self, val):
        node = Create_Node(val, self.head)
        self.head = node
    
    def insert_at_end(self, val):
        node = Create_Node(val)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = node
    
    def find_middle(self):
        slow = self.head
        fast = self.head
        if self.head == None:
            return

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.data)
    
    def traverse(self):
        current_node = self.head
        while current_node.next:
            print(current_node.data, end="->")
            current_node = current_node.next
        print(current_node.data)


# Calculating Middle element of Linked List

l1 = LinkedList(5)
l1.insert_at_begin(3)
l1.insert_at_begin(2)
l1.insert_at_begin(1)
l1.insert_at_end(6)
l1.insert_at_end(7)
l1.traverse()
l1.find_middle()