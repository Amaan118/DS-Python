class Tree:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []


    def print_tree(self):
        spaces = ' ' * self.level() * 4
        
        if self.children:
            print(f"\n{spaces}|{self.data}")
            for child in self.children:
                child.print_tree()
        else:
            print(f"{spaces}|{self.data}")


    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def level(self):
        level = 0
        while self.parent:
            self = self.parent
            level += 1
        return level
        

root = Tree("Football")

goat = Tree("GOAT")
goat.add_child(Tree("Lionel Messi"))

cf = Tree("CF")
cf.add_child(Tree("Cristiano Ronaldo"))
cf.add_child(Tree("Rober Lewa"))
cf.add_child(Tree("Luis Suarez"))
cf.add_child(Tree("Kylian Mbappe"))

cmf = Tree("CMF")
cmf.add_child(Tree("Xaviesta"))
cmf.add_child(Tree("Modric / Kroos"))
cmf.add_child(Tree("Kimmich / De Bruyne"))

cb = Tree("CB")
cb.add_child(Tree("Ramos / Varane"))
cb.add_child(Tree("Puyol / Pique"))
cb.add_child(Tree("Vidic / Rio"))

root.add_child(goat)
root.add_child(cf)
root.add_child(cmf)
root.add_child(cb)
root.print_tree()