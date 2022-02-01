from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        if self.isEmpty():
            print("Stack Empty Can't Pop")
        else:
            return self.container.pop()
            
    def traverse(self):
        if self.isEmpty():
            print("\nCan't traverse an Empty Stack")
        else:
            print("\nStack Elements are : ", end = " ")
            for i in self.container:
                print(i, end=" ")
                
    def isEmpty(self):
        if len(self.container):
            return False
        return True
        
    def size(self):
        print(f"\nSize of Stack is : {len(self.container)}")
    
    def seek(self):
        if self.isEmpty():
            return None
        return self.container[-1]
                
    def is_balanced(self, eqn):
        operator_stack = Stack()
        flag = 1
        for i in eqn:
            if i == "[" or i == "(" or i == "{":
                operator_stack.push(i)
            elif i == ")":
                if operator_stack.seek() == "(":
                    flag = 0
                    operator_stack.pop()
                else:
                    flag = 1
                    
            elif i == "]":
                if operator_stack.seek() == "[":
                    flag = 0
                    operator_stack.pop()
                else:
                    flag = 1
                    
            elif i == "}":
                if operator_stack.seek() == "{":
                    flag = 0
                    operator_stack.pop()
                else:
                    flag = 1
    
        if flag == 0 and operator_stack.isEmpty():
            return True
        return False
        
    def reverse(self, string):
        rev_str = Stack()
        new_str = []
        for i in string:
            rev_str.push(i)
        while(not rev_str.isEmpty()):
            new_str.append(rev_str.pop())
            
        return "".join(new_str)
        
s1 = Stack()
while True:
    choice = int(input("\n1.Push \n2.Pop \n3.Traverse \n4.Eqn Balance \n5.String Reverse \n6.Is Empty \n7.Size of Stack \n8.Seek \n9.Exit \n\nEnter Choice : "))
    if choice == 1:
        value = int(input("Enter Value to Push : "))
        s1.push(value)
        print(f"\n{value} successfully pushed to Stack")
    elif choice == 2:
        print(f"\nPopped Value : {s1.pop()}")
    elif choice == 3:
        s1.traverse()
    elif choice == 4:
        equ = input("Enter Equation : ")
        print(f"\n{s1.is_balanced(equ)}")
    elif choice == 5:
        str_to_rev = input("\nEnter String : ")
        print(f"\nReversed String is : {s1.reverse(str_to_rev)}")
    elif choice == 6:
        print(s1.isEmpty())
    elif choice == 7:
        s1.size()
    elif choice == 8:
        print(f"\nLast Element of Stack is : {s1.seek()}")
    else:
        exit()    