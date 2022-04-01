# Calculating Nth node from end

class Create_Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next

class LinkedList:
    def __init__(self, val):
        self.head = Create_Node(val)

    def traverse(self):
        current_node = self.head
        while current_node.next:
            print(current_node.data, end="->")
            current_node = current_node.next
        print(current_node.data)
    
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
    
    def find_nth_from_end(self, pos):
        if self.head == None:
            return
        
        current_node = self.head
        fast_node = self.head
        for i in range(pos):
            fast_node = fast_node.next
        
        while fast_node:
            current_node = current_node.next
            fast_node = fast_node.next
        print(current_node.data)

# Calculating Nth element from last of Linked List

l1 = LinkedList(5)
l1.insert_at_begin(3)
l1.insert_at_begin(2)
l1.insert_at_begin(1)
l1.insert_at_end(6)
l1.insert_at_end(7)
l1.traverse()
l1.find_nth_from_end(2)