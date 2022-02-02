class BinarySearchTree:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
        
    def add_child(self, val):
        if self.data == val:
            return
        elif val < self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTree(val)
        elif val > self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTree(val)
    
    def inOrder(self):
        traverse = []
        if self.left:
            traverse.extend(self.left.inOrder())
        traverse.append(self.data)
        if self.right:
            traverse.extend(self.right.inOrder())
            
        return traverse
        
    def preOrder(self):
        traverse = []
        traverse.append(self.data)
        if self.left:
            traverse.extend(self.left.preOrder())
        if self.right:
            traverse.extend(self.right.preOrder())
            
        return traverse
    
    def postOrder(self):
        traverse = []
        if self.left:
            traverse.extend(self.left.postOrder())
        if self.right:
            traverse.extend(self.right.postOrder())
        traverse.append(self.data)
            
        return traverse
        
    def min(self):
        if self.left:
            min = self.left.min()
        else:
            min = self.data
        
        return min
        
    def max(self):
        if self.right:
            max = self.right.max()
        else:
            max = self.data
            
        return max
        
    def search(self, val):
        if self.data == val:
            return True
        elif val < self.data:
            if self.left:
                return self.left.search(val)
        elif val > self.data:
            if self.right:
                return self.right.search(val)

    def delete(self, val):
        if not self:
            print("not")
            return self
        if val < self.data:
            self.left = self.left.delete(val)
        elif val > self.data:
            self.right = self.right.delete(val)
        else:
            if not self.right:
                return self.left
            if not self.left:
                return self.right
                
            min = self.min()
            self.data = min
            self.left.delete(min)
            #self.right = self.right.delete(self.data)
        return self

    
def construct_tree(root, items):
    for item in items:
        root.add_child(item)


root = BinarySearchTree(7)
construct_tree(root, [3,10,2,5,12])

print(root.inOrder())
root.delete(3)
print(root.inOrder())