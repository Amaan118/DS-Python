class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.data = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
     
    # Insert Methods
    
    def insert_at_beginning(self, value):
        node = Node(value, None, self.head)
        if not self.isEmpty():
            self.head.prev = node
        self.head = node

    
    def insert_at_end(self, value):
        if self.isEmpty():
            self.insert_at_beginning(value)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            
            node = Node(value, current_node)
            current_node.next = node
    
    def insert_at_index(self, index, value):
        if index==0:
            self.insert_at_beginning(value)
        elif index == self.size_of_list():
            self.insert_at_end(value)
        elif index < 0 or index > self.size_of_list():
            print("\nInvalid Index")
        else:
            current_node = self.head
            next_node = self.head.next
            count = 0
            while count != index-1:
                current_node = current_node.next
                next_node = next_node.next
                count += 1
                
            node = Node(value, current_node, next_node)
            current_node.next = node
            next_node.prev = node
            
    def insert_after_value(self, search_value, insert_value):
        if self.isEmpty():
            print("\nDoubly Linked List Empty")
        else:
            current_node = self.head
            while current_node.data != search_value:
                if current_node.next == None:
                    break
                current_node = current_node.next
            else:
                node = Node(insert_value, current_node, current_node.next)
                current_node.next = node
            
            if current_node.data == search_value and current_node.next == None:
                self.insert_at_end(insert_value)
            else:
                print("\nValue not present")

    
    # Deletion Methods
    
    def delete_at_beginning(self):
        if self.isEmpty():
            print("\nDoubly Linked List Empty")
        elif self.size_of_list() == 1:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    
    def delete_at_end(self):
        if self.isEmpty():
            print("\nDoubly Linked List Empty")
        elif self.head.next == None:
            self.head = None
        else:
            current_node = self.head
            next_node = self.head.next
            while next_node.next:
                current_node = current_node.next
                next_node = next_node.next
            
            current_node.next = None
            next_node.prev = None
    
    
    def delete_at_index(self, index):
        if index==0:
            self.delete_at_beginning()
        elif index == self.size_of_list()-1:
            self.delete_at_end()
        elif index < 0 or index >= self.size_of_list():
            print("\nInvalid Index")
        else:
            current_node = self.head
            next_node = self.head.next
            count = 0
            while count != index-1:
                current_node = current_node.next
                next_node = next_node.next
                count += 1
                
            current_node.next = next_node.next
            next_node.next.prev = current_node

    
    def delete_by_value(self, value):
        if self.isEmpty():
            print("\nDoubly Linked List Empty")
        else:
            current_node = self.head
            next_node = self.head.next
            if current_node.data == value:
                self.delete_at_beginning()
            else:
                while next_node.next:
                    if next_node.data == value:
                        current_node.next = next_node.next
                        next_node.next.prev = current_node
                        break
               
                    current_node = current_node.next
                    next_node = next_node.next
                
                if next_node.data == value:
                    self.delete_at_end()
                else:
                    print("\nValue Not Present")
    
    # Traversal Methods
    
    def print_list(self):
        if self.isEmpty():
            print("\nDoubly Linked List Empty")
        else:
            current_node = self.head
            list_str = ''
            while current_node.next != None:
                list_str += str(current_node.data) + ' --> '
                current_node = current_node.next
            
            list_str += str(current_node.data)
            return list_str

    
    def traverse_backward(self):
        if self.isEmpty():
            print("\nDoubly Linked List Empty")
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            
            list_str = ''
            while current_node.prev:
                list_str += str(current_node.data) + ' --> '
                current_node = current_node.prev
            
            list_str += str(current_node.data)
            
            return list_str
     
       
    def size_of_list(self):
        if self.isEmpty():
            print("\nDoubly Linked List Empty")
        else:
            current_node = self.head
            size = 0
            while current_node:
                size += 1
                current_node = current_node.next
            
            return size
    
    def isEmpty(self):
        return self.head == None


d1 = DoublyLinkedList()


while True:
    choice = int(input("\n1.Insert At Beginning \n2.Insert At End \n3.Insert At Index \n4.Insert after Value \n5.Delete At Beginning \n6.Delete At End \n7.Delete At Index \n8.Delete by Value \n9.Traverse Forwards \n10.Traverse Backwards \n11.Size \n0.Exit \n\nEnter Choice : "))
    
    if choice == 1:
        value = int(input("Enter Value : "))
        d1.insert_at_beginning(value)
        print(f"\nDoubly Linked List : {d1.print_list()}")
        
    elif choice == 2:
        value = int(input("Enter Value : "))
        d1.insert_at_end(value)
        print(f"\nDoubly Linked List : {d1.print_list()}")
        
    elif choice == 3:
        index = int(input("Enter Index : "))
        value = int(input("Enter Value : "))
        d1.insert_at_index(index, value)
        print(f"\nDoubly Linked List : {d1.print_list()}")
        
    elif choice == 4:
        search_value = int(input("Enter Value to Search : "))
        insert_value = int(input("Enter Value to Insert : "))
        d1.insert_after_value(search_value, insert_value)
        print(f"\nDoubly Linked List : {d1.print_list()}")
        
    elif choice == 5:
        d1.delete_at_beginning()
        print(f"\nDoubly Linked List : {d1.print_list()}")
    
    elif choice == 6:
        d1.delete_at_end()
        print(f"\nDoubly Linked List : {d1.print_list()}")
        
    elif choice == 7:
        index = int(input("Enter Index : "))
        d1.delete_at_index(index)
        print(f"\nDoubly Linked List : {d1.print_list()}")
        
    elif choice == 8:
        value = int(input("Enter Value : "))
        d1.delete_by_value(value)
        print(f"\nDoubly Linked List : {d1.print_list()}")
        
    elif choice == 9:
        print(f"\nDoubly Linked List : {d1.print_list()}")
    
    elif choice == 10:
        print(f"\nDoubly Linked List : {d1.traverse_backward()}")
    
    elif choice == 11:
        print(d1.size_of_list())
        
    else:
        exit()