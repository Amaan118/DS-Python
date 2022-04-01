# Finding Loop in LL

# Fast, Slow Pointer Method
# Run two nodes fast, slow fast steps two nodes, slow steps one node at a time
# If fast and slow are equal after certain time then Loop is present

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
    
    def create_loop(self):
        current = self.head
        while current.next:
            current = current.next
        current.next = self.head
    
    
    def traverse(self):
        current_node = self.head
        while current_node.next:
            print(current_node.data, end="->")
            current_node = current_node.next
        print(current_node.data)
    
    
    def find_loop(self):
        if self.head == None:
            print(False)
            return
        
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                print(True)
                return
        print(False)
            
    
    def traverse_loop(self):
        current = self.head
        for i in range(20):
            print(current.data, end="->")
            current = current.next


l1 = LinkedList(5)
l1.insert_at_begin(3)
l1.insert_at_begin(2)
l1.insert_at_begin(1)
l1.insert_at_end(6)
l1.insert_at_end(7)

# Creates a Loop in our Linked List
l1.create_loop()

# Traverse the Linked List for 20 times no matter the size
l1.traverse_loop()

# Prints True if 
l1.find_loop()