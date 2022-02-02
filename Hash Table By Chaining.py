class Hash:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(10)]


    def hash_function(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.MAX


    def __getitem__(self, key):
        index = self.hash_function(key)
        for tup in self.arr[index]:
            if tup[0] == key:
                return tup[1]
        return None


    def __setitem__(self, key, value):
        index = self.hash_function(key)
        present = False
        for ind, tup in enumerate(self.arr[index]):
            if key == tup[0]:
                present = True
                self.arr[index][ind] = (key, value)
        if not present:  
            self.arr[index].append((key, value))


    def get(self, key, message=None):
        index = self.hash_function(key)
        for tup in self.arr[index]:
            if tup[0] == key:
                return tup[1]
        return message
        

    def remove_key(self, key):
        index = self.hash_function(key)
        found = False
        for ind,tup in enumerate(self.arr[index]):
            if tup[0] == key:
                found = True
                del self.arr[index][ind]
        if not found:
            print(f"{key} not present")


    def print_dict(self):
        print("\nHash Table : ")
        for element in self.arr:
            print(element)


h1 = Hash()
names = ["Sameer", "Zaheer", "Azhar", "Mazhar", "Badiuddin", "Bahuddin", "Zeba", "Farhan", "Amaan", "Mehwish", "Laiqa", "Junaid", "Safura", "Nuseba", "Shahana", "Navid", "Shaziya", "Fahim", "Faizan", "Almas", "Aamena"]

for name in names:
    h1[name] = len(name)

h1.print_dict()
#h1.remove_key('Aman')
print(h1["Amaan"])
h1["Amaan"] = 63