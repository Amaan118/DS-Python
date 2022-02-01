class Node:
    def __init__(self, node_val=None, next=None):
        self.data = node_val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def size(self):
        if self.head == None:
            return 0
        current_node = self.head
        size = 0
        while current_node.next != None:
            size += 1
            current_node = current_node.next
            
        return size+1

        
    def insert_at_beginning(self, value):
        node = Node(value, self.head)
        self.head = node

                
    def insert_at_index(self, index, value):
        if self.head == None:
            self.head = Node(value)
        elif index < 0 or index > self.size():
            print("\nIndex Out of Bound")
        elif index == 0:
            self.insert_at_beginning(value)
        elif index == self.size():
            self.insert_at_end(value)
        else:
            current_node = self.head
            count = 0
            while count != index - 1:
                current_node = current_node.next
                count += 1
            
            node = Node(value, current_node.next)
            current_node.next = node         
        
        
    def insert_at_end(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
                
            node = Node(value)
            current_node.next = node


    def insert_after_value(self, search_value, insert_value):
        if self.head == None:
            print("\nLinked List Empty")
        else:
            current_node = self.head
            found = 0
            while current_node.data != search_value and current_node.next != None:
                found = 1
                current_node = current_node.next
            
            if found and current_node.data == search_value:
                node = Node(insert_value, current_node.next)
                current_node.next = node
            else:
                print(f"\n{search_value} not in Linked List")


    def delete_at_beginning(self):
        if self.head == None:
            print("\nLinked List Empty")
        else:
            self.head = self.head.next 


    def delete_at_end(self):
        if self.head == None:
            print("\nLinked List Empty")
        elif self.head.next == None:
            self.head = None
        else:
            current_node = self.head
            next_node = self.head.next
            while next_node.next != None:
                current_node = current_node.next
                next_node = next_node.next
            
            current_node.next = None


    def delete_at_index(self, index):
        if self.head == None:
            print("\nLinked List Empty")
        elif index < 0 or index >= self.size():
            print("\nIndex Out of Bound")
        elif index == 0:
            self.delete_at_beginning()
        elif index == self.size()-1:
            self.delete_at_end()
        else:
            current_node = self.head
            count = 0
            while count != index - 1:
                current_node = current_node.next
                count += 1
            
            current_node.next = current_node.next.next


    def delete_by_value(self, value):
        if self.head == None:
            print("\nLinked List Empty")
        elif self.head.data == value:
            self.delete_at_beginning()
        else:
            current_node = self.head
            next_node = self.head.next
            found = 0
            while next_node.next != None and next_node.data != value:
                found = 1
                current_node = current_node.next
                next_node = next_node.next
            
            if next_node.data == value:
                found = 1
                current_node.next = None
                
            if found:
                current_node.next = next_node.next
            else:
                print(f"\n{value} not present in Linked List")


    def print_linked_list(self):
        if self.head == None:
            print("\nLinked List Empty")
        else:
            current_node = self.head
            list_str = ''
            while current_node.next != None:
                list_str += str(current_node.data) + ' --> '
                current_node = current_node.next
            
            list_str += str(current_node.data)
            return list_str
    
    

l1 = LinkedList()

while True:
    choice = int(input("\n1.Insert At Beginning \n2.Insert At End \n3.Insert At Index \n4.Insert after Value \n5.Delete At Beginning \n6.Delete At End \n7.Delete At Index \n8.Delete by Value \n9.Traverse \n10. Size \n11.Exit \n\nEnter Choice : "))
    
    if choice == 1:
        value = int(input("Enter Value : "))
        l1.insert_at_beginning(value)
        print(f"\nLinked List : {l1.print_linked_list()}")
        
    elif choice == 2:
        value = int(input("Enter Value : "))
        l1.insert_at_end(value)
        print(f"\nLinked List : {l1.print_linked_list()}")
        
    elif choice == 3:
        index = int(input("Enter Index : "))
        value = int(input("Enter Value : "))
        l1.insert_at_index(index, value)
        print(f"\nLinked List : {l1.print_linked_list()}")
        
    elif choice == 4:
        search_value = int(input("Enter Value to Search : "))
        insert_value = int(input("Enter Value to Search : "))
        l1.insert_after_value(search_value, insert_value)
        print(f"\nLinked List : {l1.print_linked_list()}")
        
    elif choice == 5:
        l1.delete_at_beginning()
        print(f"\nLinked List : {l1.print_linked_list()}")
        
    elif choice == 6:
        l1.delete_at_end()
        print(f"\nLinked List : {l1.print_linked_list()}")
        
    elif choice == 7:
        index = int(input("Enter Index : "))
        l1.delete_at_index(index)
        print(f"\nLinked List : {l1.print_linked_list()}")
        
    elif choice == 8:
        value = int(input("Enter Value : "))
        l1.delete_by_value(value)
        print(f"\nLinked List : {l1.print_linked_list()}")
        
    elif choice == 9:
        print(f"\nLinked List : {l1.print_linked_list()}")
        
    elif choice == 10:
        print(l1.size())
        
    else:
        exit()